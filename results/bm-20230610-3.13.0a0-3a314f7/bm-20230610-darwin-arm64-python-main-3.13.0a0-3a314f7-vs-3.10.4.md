
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3a314f7
- commit date: 2023-06-10
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.54 sec: 1.16x faster                                |
| tornado_http   | 91.9 ms                                                | 70.8 ms: 1.30x faster                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 71.6 ms: 1.31x faster                                 |
| float          | 72.3 ms                                                | 56.6 ms: 1.28x faster                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.9 ms: 1.27x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.62 ms: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 186 us: 1.53x faster                                  |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.55 ms: 1.28x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                |
| xml_etree_process    | 45.1 ms                                                | 38.9 ms: 1.16x faster                                 |
| unpickle             | 9.77 us                                                | 9.33 us: 1.05x faster                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                 |
| pickle_list          | 2.83 us                                                | 2.91 us: 1.03x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 74.9 ms: 1.03x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 56.3 ms: 1.04x slower                                 |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.20 us: 1.20x slower                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.7 ms: 1.08x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 9.66 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.55 ms: 1.39x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 91.1 us: 3.78x faster                                 |
| deltablue                | 5.15 ms                                                | 2.43 ms: 2.11x faster                                 |
| logging_silent           | 119 ns                                                 | 66.6 ns: 1.79x faster                                 |
| richards_super           | 60.7 ms                                                | 34.8 ms: 1.74x faster                                 |
| go                       | 165 ms                                                 | 96.5 ms: 1.71x faster                                 |
| richards                 | 51.4 ms                                                | 31.2 ms: 1.65x faster                                 |
| sqlglot_parse            | 1.33 ms                                                | 823 us: 1.62x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 998 us: 1.54x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 439 ms: 1.53x faster                                  |
| pickle_pure_python       | 284 us                                                 | 186 us: 1.53x faster                                  |
| chaos                    | 66.8 ms                                                | 43.9 ms: 1.52x faster                                 |
| crypto_pyaes             | 78.0 ms                                                | 51.5 ms: 1.52x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 328 ms: 1.50x faster                                  |
| scimark_sor              | 127 ms                                                 | 84.8 ms: 1.49x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                 |
| scimark_lu               | 110 ms                                                 | 73.7 ms: 1.49x faster                                 |
| async_tree_io            | 1.02 sec                                               | 701 ms: 1.45x faster                                  |
| async_tree_none          | 402 ms                                                 | 280 ms: 1.44x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 50.5 ms: 1.43x faster                                 |
| unpickle_pure_python     | 203 us                                                 | 145 us: 1.40x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 27.8 ns: 1.39x faster                                 |
| mako                     | 10.5 ms                                                | 7.55 ms: 1.39x faster                                 |
| pyflate                  | 453 ms                                                 | 328 ms: 1.38x faster                                  |
| raytrace                 | 328 ms                                                 | 242 ms: 1.36x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 25.4 us: 1.35x faster                                 |
| pycparser                | 915 ms                                                 | 680 ms: 1.35x faster                                  |
| nbody                    | 94.1 ms                                                | 71.6 ms: 1.31x faster                                 |
| tornado_http             | 91.9 ms                                                | 70.8 ms: 1.30x faster                                 |
| spectral_norm            | 96.4 ms                                                | 74.3 ms: 1.30x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.27 sec: 1.29x faster                                |
| logging_format           | 5.01 us                                                | 3.90 us: 1.29x faster                                 |
| json_dumps               | 8.38 ms                                                | 6.55 ms: 1.28x faster                                 |
| logging_simple           | 4.63 us                                                | 3.62 us: 1.28x faster                                 |
| float                    | 72.3 ms                                                | 56.6 ms: 1.28x faster                                 |
| regex_compile            | 96.6 ms                                                | 75.9 ms: 1.27x faster                                 |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                |
| generators               | 32.9 ms                                                | 26.0 ms: 1.27x faster                                 |
| create_gc_cycles         | 876 us                                                 | 704 us: 1.24x faster                                  |
| dulwich_log              | 37.1 ms                                                | 29.9 ms: 1.24x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 543 ms: 1.23x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 1.01 sec: 1.23x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 498 ms: 1.22x faster                                  |
| mypy2                    | 308 ms                                                 | 258 ms: 1.19x faster                                  |
| deepcopy                 | 278 us                                                 | 233 us: 1.19x faster                                  |
| fannkuch                 | 317 ms                                                 | 269 ms: 1.18x faster                                  |
| coroutines               | 20.2 ms                                                | 17.3 ms: 1.17x faster                                 |
| xml_etree_process        | 45.1 ms                                                | 38.9 ms: 1.16x faster                                 |
| docutils                 | 1.78 sec                                               | 1.54 sec: 1.16x faster                                |
| scimark_fft              | 232 ms                                                 | 202 ms: 1.15x faster                                  |
| nqueens                  | 68.1 ms                                                | 59.6 ms: 1.14x faster                                 |
| bench_thread_pool        | 548 us                                                 | 483 us: 1.14x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.12 us: 1.12x faster                                 |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 34.0 ms: 1.12x faster                                 |
| comprehensions           | 17.7 us                                                | 16.0 us: 1.10x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.15 ms: 1.10x faster                                 |
| python_startup           | 12.6 ms                                                | 11.7 ms: 1.08x faster                                 |
| meteor_contest           | 78.6 ms                                                | 73.5 ms: 1.07x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                  |
| regex_dna                | 160 ms                                                 | 151 ms: 1.06x faster                                  |
| unpickle                 | 9.77 us                                                | 9.33 us: 1.05x faster                                 |
| json                     | 3.10 ms                                                | 2.99 ms: 1.03x faster                                 |
| mdp                      | 1.67 sec                                               | 1.62 sec: 1.03x faster                                |
| python_startup_no_site   | 9.73 ms                                                | 9.66 ms: 1.01x faster                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                  |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| pickle                   | 7.36 us                                                | 7.42 us: 1.01x slower                                 |
| pickle_list              | 2.83 us                                                | 2.91 us: 1.03x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 74.9 ms: 1.03x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 56.3 ms: 1.04x slower                                 |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| telco                    | 3.68 ms                                                | 3.87 ms: 1.05x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.56 us: 1.06x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.62 ms: 1.07x slower                                 |
| pathlib                  | 28.8 ms                                                | 31.0 ms: 1.08x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 45.2 ms: 1.10x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.20 us: 1.20x slower                                 |
| coverage                 | 40.8 ms                                                | 50.6 ms: 1.24x slower                                 |
| async_generators         | 233 ms                                                 | 311 ms: 1.33x slower                                  |
| Geometric mean           | (ref)                                                  | 1.23x faster                                          |
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
