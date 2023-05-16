
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: 4d1b4d4
- commit date: 2023-05-12
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.02x faster                                                                   |
| tornado_http   | 122 ms                                                       | 113 ms: 1.07x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.6 ms: 1.06x faster                                                                  |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                                                   |
| float          | 74.2 ms                                                      | 77.7 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                                                   |
| regex_v8       | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.50 ms                                                      | 3.52 ms: 1.01x slower                                                                  |
| regex_dna      | 227 ms                                                       | 230 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                                  |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.20x faster                                                                  |
| unpickle_pure_python | 241 us                                                       | 204 us: 1.18x faster                                                                   |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.08x faster                                                                   |
| tomli_loads          | 2.26 sec                                                     | 2.16 sec: 1.05x faster                                                                 |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.00x slower                                                                   |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                                                   |
| pickle_dict          | 30.8 us                                                      | 32.0 us: 1.04x slower                                                                  |
| xml_etree_process    | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                                                  |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                                  |
| xml_etree_generate   | 80.5 ms                                                      | 85.3 ms: 1.06x slower                                                                  |
| unpickle             | 13.4 us                                                      | 14.3 us: 1.06x slower                                                                  |
| unpickle_list        | 4.53 us                                                      | 4.88 us: 1.08x slower                                                                  |
| pickle_list          | 3.83 us                                                      | 4.32 us: 1.13x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                                                  |
| python_startup_no_site | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|-----------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.89 ms: 1.11x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                                                   |
| asyncio_tcp              | 753 ms                                                       | 380 ms: 1.98x faster                                                                   |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                                                 |
| generators               | 56.0 ms                                                      | 35.7 ms: 1.57x faster                                                                  |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                                  |
| chaos                    | 80.9 ms                                                      | 63.6 ms: 1.27x faster                                                                  |
| deltablue                | 4.00 ms                                                      | 3.20 ms: 1.25x faster                                                                  |
| hexiom                   | 7.13 ms                                                      | 5.79 ms: 1.23x faster                                                                  |
| coroutines               | 27.6 ms                                                      | 22.4 ms: 1.23x faster                                                                  |
| richards_super           | 61.0 ms                                                      | 50.1 ms: 1.22x faster                                                                  |
| fannkuch                 | 429 ms                                                       | 356 ms: 1.20x faster                                                                   |
| json_loads               | 28.7 us                                                      | 24.0 us: 1.20x faster                                                                  |
| unpickle_pure_python     | 241 us                                                       | 204 us: 1.18x faster                                                                   |
| scimark_lu               | 115 ms                                                       | 98.0 ms: 1.17x faster                                                                  |
| async_tree_memoization   | 630 ms                                                       | 550 ms: 1.15x faster                                                                   |
| nqueens                  | 103 ms                                                       | 90.3 ms: 1.14x faster                                                                  |
| comprehensions           | 24.6 us                                                      | 21.7 us: 1.14x faster                                                                  |
| go                       | 164 ms                                                       | 144 ms: 1.14x faster                                                                   |
| async_tree_none          | 519 ms                                                       | 458 ms: 1.13x faster                                                                   |
| async_tree_io            | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                                                 |
| logging_silent           | 101 ns                                                       | 90.5 ns: 1.11x faster                                                                  |
| mako                     | 11.0 ms                                                      | 9.89 ms: 1.11x faster                                                                  |
| richards                 | 48.3 ms                                                      | 43.5 ms: 1.11x faster                                                                  |
| sqlglot_parse            | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                                                  |
| logging_format           | 8.11 us                                                      | 7.32 us: 1.11x faster                                                                  |
| regex_compile            | 158 ms                                                       | 143 ms: 1.10x faster                                                                   |
| json                     | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                                                  |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                                                 |
| deepcopy_memo            | 38.8 us                                                      | 35.9 us: 1.08x faster                                                                  |
| logging_simple           | 7.19 us                                                      | 6.67 us: 1.08x faster                                                                  |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.08x faster                                                                   |
| pycparser                | 1.32 sec                                                     | 1.23 sec: 1.08x faster                                                                 |
| sqlglot_transpile        | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                                                  |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.08x faster                                                                   |
| tornado_http             | 122 ms                                                       | 113 ms: 1.07x faster                                                                   |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 698 ms: 1.07x faster                                                                   |
| deepcopy                 | 399 us                                                       | 373 us: 1.07x faster                                                                   |
| nbody                    | 90.7 ms                                                      | 85.6 ms: 1.06x faster                                                                  |
| bench_thread_pool        | 1.01 ms                                                      | 958 us: 1.06x faster                                                                   |
| crypto_pyaes             | 83.4 ms                                                      | 79.5 ms: 1.05x faster                                                                  |
| dulwich_log              | 68.4 ms                                                      | 65.3 ms: 1.05x faster                                                                  |
| raytrace                 | 317 ms                                                       | 302 ms: 1.05x faster                                                                   |
| tomli_loads              | 2.26 sec                                                     | 2.16 sec: 1.05x faster                                                                 |
| spectral_norm            | 93.3 ms                                                      | 89.5 ms: 1.04x faster                                                                  |
| deepcopy_reduce          | 3.51 us                                                      | 3.39 us: 1.04x faster                                                                  |
| scimark_sor              | 111 ms                                                       | 107 ms: 1.03x faster                                                                   |
| sqlglot_optimize         | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                                  |
| pyflate                  | 449 ms                                                       | 441 ms: 1.02x faster                                                                   |
| 2to3                     | 288 ms                                                       | 283 ms: 1.02x faster                                                                   |
| regex_v8                 | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                                  |
| pprint_pformat           | 1.63 sec                                                     | 1.61 sec: 1.01x faster                                                                 |
| gc_traversal             | 3.85 ms                                                      | 3.80 ms: 1.01x faster                                                                  |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.01x faster                                                                   |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.5 ms: 1.00x slower                                                                  |
| pickle_pure_python       | 319 us                                                       | 321 us: 1.00x slower                                                                   |
| pprint_safe_repr         | 784 ms                                                       | 788 ms: 1.00x slower                                                                   |
| regex_effbot             | 3.50 ms                                                      | 3.52 ms: 1.01x slower                                                                  |
| xml_etree_iterparse      | 104 ms                                                       | 105 ms: 1.01x slower                                                                   |
| regex_dna                | 227 ms                                                       | 230 ms: 1.01x slower                                                                   |
| pathlib                  | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                                  |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                                                   |
| pickle_dict              | 30.8 us                                                      | 32.0 us: 1.04x slower                                                                  |
| xml_etree_process        | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                                                  |
| telco                    | 6.86 ms                                                      | 7.16 ms: 1.04x slower                                                                  |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                                                  |
| float                    | 74.2 ms                                                      | 77.7 ms: 1.05x slower                                                                  |
| scimark_fft              | 285 ms                                                       | 300 ms: 1.05x slower                                                                   |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                                                  |
| xml_etree_generate       | 80.5 ms                                                      | 85.3 ms: 1.06x slower                                                                  |
| sqlite_synth             | 2.50 us                                                      | 2.65 us: 1.06x slower                                                                  |
| unpickle                 | 13.4 us                                                      | 14.3 us: 1.06x slower                                                                  |
| coverage                 | 84.8 ms                                                      | 90.5 ms: 1.07x slower                                                                  |
| unpickle_list            | 4.53 us                                                      | 4.88 us: 1.08x slower                                                                  |
| python_startup_no_site   | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                                  |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.40 ms: 1.09x slower                                                                  |
| bench_mp_pool            | 4.62 ms                                                      | 5.15 ms: 1.11x slower                                                                  |
| pickle_list              | 3.83 us                                                      | 4.32 us: 1.13x slower                                                                  |
| unpack_sequence          | 45.6 ns                                                      | 51.6 ns: 1.13x slower                                                                  |
| async_generators         | 316 ms                                                       | 386 ms: 1.22x slower                                                                   |
| dask                     | 410 ms                                                       | 556 ms: 1.35x slower                                                                   |
| Geometric mean           | (ref)                                                        | 1.08x faster                                                                           |

Benchmark hidden because not significant (3): docutils, mypy2, create_gc_cycles
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
