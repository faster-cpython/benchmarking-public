
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: a4e456f
- commit date: 2023-06-22
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                  |
| float          | 77.2 ms                                                | 79.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                 |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                  |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                 |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.86 ms: 1.28x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.06x faster                                                  |
| json_loads           | 26.5 us                                                | 25.1 us: 1.05x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| tomli_loads          | 2.22 sec                                               | 2.21 sec: 1.01x faster                                                |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                                 |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.7 us: 1.07x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.50 us: 1.10x slower                                                 |
| unpickle             | 13.7 us                                                | 15.3 us: 1.12x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 85.2 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.17 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 150 us: 3.25x faster                                                  |
| generators               | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.86 ms: 1.28x faster                                                 |
| mypy2                    | 420 ms                                                 | 337 ms: 1.25x faster                                                  |
| chaos                    | 69.2 ms                                                | 58.9 ms: 1.17x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.28 ms: 1.12x faster                                                 |
| richards_super           | 56.8 ms                                                | 51.7 ms: 1.10x faster                                                 |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                                  |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                                 |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.07x faster                                                 |
| coverage                 | 100 ms                                                 | 93.1 ms: 1.07x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 589 ms: 1.06x faster                                                  |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.06x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.05x faster                                                 |
| json_loads               | 26.5 us                                                | 25.1 us: 1.05x faster                                                 |
| nqueens                  | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.12 ms: 1.04x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                |
| mdp                      | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                 |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                                  |
| unpack_sequence          | 43.1 ns                                                | 41.8 ns: 1.03x faster                                                 |
| logging_format           | 6.68 us                                                | 6.49 us: 1.03x faster                                                 |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| xml_etree_parse          | 158 ms                                                 | 155 ms: 1.02x faster                                                  |
| regex_compile            | 138 ms                                                 | 135 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 725 ms: 1.02x faster                                                  |
| logging_simple           | 6.03 us                                                | 5.93 us: 1.02x faster                                                 |
| sqlglot_optimize         | 53.1 ms                                                | 52.4 ms: 1.01x faster                                                 |
| logging_silent           | 101 ns                                                 | 100 ns: 1.01x faster                                                  |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.01x faster                                                  |
| tomli_loads              | 2.22 sec                                               | 2.21 sec: 1.01x faster                                                |
| regex_dna                | 204 ms                                                 | 203 ms: 1.00x faster                                                  |
| pickle_dict              | 31.1 us                                                | 31.2 us: 1.00x slower                                                 |
| bench_thread_pool        | 819 us                                                 | 822 us: 1.00x slower                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.55 ms: 1.01x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                 |
| pickle_pure_python       | 306 us                                                 | 311 us: 1.02x slower                                                  |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                                  |
| fannkuch                 | 388 ms                                                 | 398 ms: 1.03x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 721 ms: 1.03x slower                                                  |
| float                    | 77.2 ms                                                | 79.9 ms: 1.03x slower                                                 |
| crypto_pyaes             | 74.7 ms                                                | 77.4 ms: 1.04x slower                                                 |
| pathlib                  | 18.2 ms                                                | 18.9 ms: 1.04x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 66.0 ms: 1.04x slower                                                 |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                  |
| telco                    | 6.58 ms                                                | 6.88 ms: 1.04x slower                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 71.2 ms: 1.05x slower                                                 |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                 |
| pickle                   | 10.1 us                                                | 10.7 us: 1.07x slower                                                 |
| scimark_fft              | 328 ms                                                 | 351 ms: 1.07x slower                                                  |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                                  |
| gc_traversal             | 4.02 ms                                                | 4.31 ms: 1.07x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.17 ms: 1.08x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.17 us: 1.08x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.50 us: 1.10x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.67 ms: 1.11x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.3 us: 1.12x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 85.2 ms: 1.12x slower                                                 |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                                  |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (7): meteor_contest, nbody, richards, bench_mp_pool, tornado_http, scimark_sor, unpickle_list
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
