
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.53 sec: 1.17x faster                                |
| tornado_http   | 91.9 ms                                                | 71.9 ms: 1.28x faster                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 72.3 ms: 1.30x faster                                 |
| float          | 72.3 ms                                                | 56.4 ms: 1.28x faster                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 79.1 ms: 1.22x faster                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.08x faster                                  |
| regex_v8       | 17.5 ms                                                | 17.0 ms: 1.03x faster                                 |
| regex_effbot   | 2.45 ms                                                | 2.57 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 198 us: 1.43x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.58 ms: 1.27x faster                                 |
| unpickle_pure_python | 203 us                                                 | 163 us: 1.25x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.57 sec: 1.12x faster                                |
| xml_etree_process    | 45.1 ms                                                | 40.7 ms: 1.11x faster                                 |
| unpickle             | 9.77 us                                                | 9.17 us: 1.06x faster                                 |
| pickle               | 7.36 us                                                | 7.41 us: 1.01x slower                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                  |
| pickle_list          | 2.83 us                                                | 2.90 us: 1.03x slower                                 |
| json_loads           | 16.9 us                                                | 17.4 us: 1.03x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 76.5 ms: 1.05x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 59.0 ms: 1.09x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.14 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.3 ms: 1.11x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 9.18 ms: 1.06x faster                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.54 ms: 1.39x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 94.1 us: 3.65x faster                                 |
| deltablue                | 5.15 ms                                                | 2.54 ms: 2.03x faster                                 |
| raytrace                 | 328 ms                                                 | 189 ms: 1.73x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 405 ms: 1.66x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 47.9 ms: 1.63x faster                                 |
| logging_silent           | 119 ns                                                 | 73.6 ns: 1.62x faster                                 |
| sqlglot_parse            | 1.33 ms                                                | 827 us: 1.61x faster                                  |
| chaos                    | 66.8 ms                                                | 42.2 ms: 1.59x faster                                 |
| async_tree_none          | 402 ms                                                 | 257 ms: 1.57x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 46.4 ms: 1.56x faster                                 |
| richards_super           | 60.7 ms                                                | 39.5 ms: 1.54x faster                                 |
| sqlglot_transpile        | 1.54 ms                                                | 1.01 ms: 1.53x faster                                 |
| go                       | 165 ms                                                 | 108 ms: 1.53x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 332 ms: 1.48x faster                                  |
| scimark_lu               | 110 ms                                                 | 76.2 ms: 1.44x faster                                 |
| async_tree_io            | 1.02 sec                                               | 709 ms: 1.44x faster                                  |
| pickle_pure_python       | 284 us                                                 | 198 us: 1.43x faster                                  |
| richards                 | 51.4 ms                                                | 36.1 ms: 1.42x faster                                 |
| unpack_sequence          | 38.7 ns                                                | 27.5 ns: 1.40x faster                                 |
| mako                     | 10.5 ms                                                | 7.54 ms: 1.39x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 24.9 us: 1.39x faster                                 |
| pyflate                  | 453 ms                                                 | 348 ms: 1.30x faster                                  |
| pycparser                | 915 ms                                                 | 703 ms: 1.30x faster                                  |
| nbody                    | 94.1 ms                                                | 72.3 ms: 1.30x faster                                 |
| spectral_norm            | 96.4 ms                                                | 74.2 ms: 1.30x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.87 ms: 1.30x faster                                 |
| float                    | 72.3 ms                                                | 56.4 ms: 1.28x faster                                 |
| tornado_http             | 91.9 ms                                                | 71.9 ms: 1.28x faster                                 |
| json_dumps               | 8.38 ms                                                | 6.58 ms: 1.27x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 528 ms: 1.27x faster                                  |
| create_gc_cycles         | 876 us                                                 | 698 us: 1.25x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 163 us: 1.25x faster                                  |
| regex_compile            | 96.6 ms                                                | 79.1 ms: 1.22x faster                                 |
| logging_simple           | 4.63 us                                                | 3.80 us: 1.22x faster                                 |
| logging_format           | 5.01 us                                                | 4.12 us: 1.22x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.36 sec: 1.21x faster                                |
| deepcopy                 | 278 us                                                 | 230 us: 1.21x faster                                  |
| dulwich_log              | 37.1 ms                                                | 31.1 ms: 1.19x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 1.04 sec: 1.19x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 514 ms: 1.18x faster                                  |
| mypy2                    | 308 ms                                                 | 261 ms: 1.18x faster                                  |
| scimark_sor              | 127 ms                                                 | 108 ms: 1.17x faster                                  |
| comprehensions           | 17.7 us                                                | 15.0 us: 1.17x faster                                 |
| generators               | 32.9 ms                                                | 28.2 ms: 1.17x faster                                 |
| docutils                 | 1.78 sec                                               | 1.53 sec: 1.17x faster                                |
| deepcopy_reduce          | 2.38 us                                                | 2.06 us: 1.16x faster                                 |
| nqueens                  | 68.1 ms                                                | 59.0 ms: 1.15x faster                                 |
| scimark_fft              | 232 ms                                                 | 202 ms: 1.15x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.57 sec: 1.12x faster                                |
| bench_thread_pool        | 548 us                                                 | 491 us: 1.12x faster                                  |
| python_startup           | 12.6 ms                                                | 11.3 ms: 1.11x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.13 ms: 1.11x faster                                 |
| fannkuch                 | 317 ms                                                 | 286 ms: 1.11x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 40.7 ms: 1.11x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 35.2 ms: 1.08x faster                                 |
| regex_dna                | 160 ms                                                 | 149 ms: 1.08x faster                                  |
| unpickle                 | 9.77 us                                                | 9.17 us: 1.06x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 9.18 ms: 1.06x faster                                 |
| meteor_contest           | 78.6 ms                                                | 74.5 ms: 1.06x faster                                 |
| coroutines               | 20.2 ms                                                | 19.4 ms: 1.04x faster                                 |
| regex_v8                 | 17.5 ms                                                | 17.0 ms: 1.03x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 191 ms: 1.03x faster                                  |
| json                     | 3.10 ms                                                | 3.01 ms: 1.03x faster                                 |
| pathlib                  | 28.8 ms                                                | 28.2 ms: 1.02x faster                                 |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                  |
| gc_traversal             | 2.40 ms                                                | 2.39 ms: 1.00x faster                                 |
| pickle                   | 7.36 us                                                | 7.41 us: 1.01x slower                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                  |
| pickle_list              | 2.83 us                                                | 2.90 us: 1.03x slower                                 |
| json_loads               | 16.9 us                                                | 17.4 us: 1.03x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.57 ms: 1.05x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 76.5 ms: 1.05x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 59.0 ms: 1.09x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.62 us: 1.10x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 45.4 ms: 1.11x slower                                 |
| coverage                 | 40.8 ms                                                | 47.5 ms: 1.16x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.14 us: 1.18x slower                                 |
| telco                    | 3.68 ms                                                | 4.57 ms: 1.24x slower                                 |
| dask                     | 258 ms                                                 | 337 ms: 1.31x slower                                  |
| async_generators         | 233 ms                                                 | 308 ms: 1.32x slower                                  |
| Geometric mean           | (ref)                                                  | 1.20x faster                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
