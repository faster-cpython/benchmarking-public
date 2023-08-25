
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.52 sec: 1.17x faster                                |
| tornado_http   | 91.9 ms                                                | 71.0 ms: 1.30x faster                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 72.4 ms: 1.30x faster                                 |
| float          | 72.3 ms                                                | 56.6 ms: 1.28x faster                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 78.5 ms: 1.23x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.59 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 200 us: 1.42x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.58 ms: 1.27x faster                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.57 sec: 1.12x faster                                |
| xml_etree_process    | 45.1 ms                                                | 40.8 ms: 1.11x faster                                 |
| unpickle             | 9.77 us                                                | 9.16 us: 1.07x faster                                 |
| pickle               | 7.36 us                                                | 7.41 us: 1.01x slower                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.04x slower                                  |
| json_loads           | 16.9 us                                                | 17.5 us: 1.04x slower                                 |
| pickle_list          | 2.83 us                                                | 2.94 us: 1.04x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 76.9 ms: 1.06x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 58.6 ms: 1.08x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.3 ms: 1.12x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 9.15 ms: 1.06x faster                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.46 ms: 1.40x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 94.6 us: 3.64x faster                                 |
| deltablue                | 5.15 ms                                                | 2.53 ms: 2.04x faster                                 |
| raytrace                 | 328 ms                                                 | 188 ms: 1.74x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 47.6 ms: 1.64x faster                                 |
| logging_silent           | 119 ns                                                 | 73.7 ns: 1.62x faster                                 |
| asyncio_tcp              | 673 ms                                                 | 419 ms: 1.61x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 840 us: 1.59x faster                                  |
| chaos                    | 66.8 ms                                                | 42.3 ms: 1.58x faster                                 |
| async_tree_none          | 402 ms                                                 | 257 ms: 1.56x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 46.4 ms: 1.56x faster                                 |
| richards_super           | 60.7 ms                                                | 39.5 ms: 1.54x faster                                 |
| sqlglot_transpile        | 1.54 ms                                                | 1.01 ms: 1.53x faster                                 |
| go                       | 165 ms                                                 | 108 ms: 1.52x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 331 ms: 1.49x faster                                  |
| scimark_lu               | 110 ms                                                 | 75.4 ms: 1.46x faster                                 |
| async_tree_io            | 1.02 sec                                               | 709 ms: 1.44x faster                                  |
| richards                 | 51.4 ms                                                | 35.9 ms: 1.43x faster                                 |
| pickle_pure_python       | 284 us                                                 | 200 us: 1.42x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 27.5 ns: 1.41x faster                                 |
| mako                     | 10.5 ms                                                | 7.46 ms: 1.40x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 25.1 us: 1.38x faster                                 |
| pyflate                  | 453 ms                                                 | 348 ms: 1.30x faster                                  |
| pycparser                | 915 ms                                                 | 703 ms: 1.30x faster                                  |
| nbody                    | 94.1 ms                                                | 72.4 ms: 1.30x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.86 ms: 1.30x faster                                 |
| tornado_http             | 91.9 ms                                                | 71.0 ms: 1.30x faster                                 |
| float                    | 72.3 ms                                                | 56.6 ms: 1.28x faster                                 |
| json_dumps               | 8.38 ms                                                | 6.58 ms: 1.27x faster                                 |
| spectral_norm            | 96.4 ms                                                | 75.8 ms: 1.27x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 528 ms: 1.27x faster                                  |
| create_gc_cycles         | 876 us                                                 | 690 us: 1.27x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 162 us: 1.26x faster                                  |
| regex_compile            | 96.6 ms                                                | 78.5 ms: 1.23x faster                                 |
| logging_format           | 5.01 us                                                | 4.10 us: 1.22x faster                                 |
| logging_simple           | 4.63 us                                                | 3.82 us: 1.21x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.36 sec: 1.21x faster                                |
| dulwich_log              | 37.1 ms                                                | 31.1 ms: 1.19x faster                                 |
| deepcopy                 | 278 us                                                 | 233 us: 1.19x faster                                  |
| mypy2                    | 308 ms                                                 | 261 ms: 1.18x faster                                  |
| generators               | 32.9 ms                                                | 28.0 ms: 1.18x faster                                 |
| docutils                 | 1.78 sec                                               | 1.52 sec: 1.17x faster                                |
| scimark_sor              | 127 ms                                                 | 108 ms: 1.17x faster                                  |
| comprehensions           | 17.7 us                                                | 15.1 us: 1.17x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 1.07 sec: 1.16x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 528 ms: 1.15x faster                                  |
| scimark_fft              | 232 ms                                                 | 202 ms: 1.15x faster                                  |
| nqueens                  | 68.1 ms                                                | 59.6 ms: 1.14x faster                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.11 us: 1.13x faster                                 |
| tomli_loads              | 1.76 sec                                               | 1.57 sec: 1.12x faster                                |
| python_startup           | 12.6 ms                                                | 11.3 ms: 1.12x faster                                 |
| fannkuch                 | 317 ms                                                 | 284 ms: 1.12x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| bench_thread_pool        | 548 us                                                 | 493 us: 1.11x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.14 ms: 1.11x faster                                 |
| xml_etree_process        | 45.1 ms                                                | 40.8 ms: 1.11x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 35.3 ms: 1.08x faster                                 |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                  |
| unpickle                 | 9.77 us                                                | 9.16 us: 1.07x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 9.15 ms: 1.06x faster                                 |
| meteor_contest           | 78.6 ms                                                | 74.6 ms: 1.05x faster                                 |
| coroutines               | 20.2 ms                                                | 19.5 ms: 1.04x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 191 ms: 1.03x faster                                  |
| json                     | 3.10 ms                                                | 3.03 ms: 1.02x faster                                 |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                |
| gc_traversal             | 2.40 ms                                                | 2.39 ms: 1.00x faster                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                  |
| pickle                   | 7.36 us                                                | 7.41 us: 1.01x slower                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.04x slower                                  |
| json_loads               | 16.9 us                                                | 17.5 us: 1.04x slower                                 |
| pickle_list              | 2.83 us                                                | 2.94 us: 1.04x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.59 ms: 1.06x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 76.9 ms: 1.06x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.59 us: 1.08x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 58.6 ms: 1.08x slower                                 |
| pathlib                  | 28.8 ms                                                | 31.3 ms: 1.09x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 45.3 ms: 1.10x slower                                 |
| coverage                 | 40.8 ms                                                | 47.6 ms: 1.17x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| telco                    | 3.68 ms                                                | 4.53 ms: 1.23x slower                                 |
| dask                     | 258 ms                                                 | 336 ms: 1.30x slower                                  |
| async_generators         | 233 ms                                                 | 310 ms: 1.33x slower                                  |
| Geometric mean           | (ref)                                                  | 1.20x faster                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
