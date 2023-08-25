
# Results vs. 3.11.0

- fork: kumaraditya303
- ref: linked_list
- machine: linux-x86_64
- commit hash: 1d32835
- commit date: 2023-08-05
- overall geometric mean: 1.05x faster
- HPT reliability: 93.44%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                               |
| tornado_http   | 96.3 ms                                                | 94.8 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.4 ms: 1.07x faster                                                |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                 |
| float          | 77.2 ms                                                | 79.4 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                                |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                 |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                 |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                                 |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                |
| pickle_pure_python   | 306 us                                                 | 295 us: 1.04x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                |
| tomli_loads          | 2.22 sec                                               | 2.32 sec: 1.04x slower                                               |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                                |
| xml_etree_process    | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 83.9 ms: 1.10x slower                                                |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                                |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.40 ms: 1.10x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 6.87 ms: 1.14x slower                                                |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.30x faster                                                 |
| generators               | 73.5 ms                                                | 28.2 ms: 2.61x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 483 ms: 1.91x faster                                                 |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                               |
| async_tree_none          | 526 ms                                                 | 405 ms: 1.30x faster                                                 |
| json_dumps               | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                |
| mypy2                    | 420 ms                                                 | 335 ms: 1.25x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.2 ms: 1.17x faster                                                |
| async_tree_memoization   | 627 ms                                                 | 540 ms: 1.16x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                |
| regex_effbot             | 3.99 ms                                                | 3.47 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 643 ms: 1.15x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                |
| async_tree_io            | 1.30 sec                                               | 1.14 sec: 1.13x faster                                               |
| raytrace                 | 297 ms                                                 | 267 ms: 1.11x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                                |
| crypto_pyaes             | 74.7 ms                                                | 68.6 ms: 1.09x faster                                                |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                                 |
| richards_super           | 56.8 ms                                                | 52.6 ms: 1.08x faster                                                |
| coverage                 | 100 ms                                                 | 93.1 ms: 1.08x faster                                                |
| hexiom                   | 6.37 ms                                                | 5.95 ms: 1.07x faster                                                |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.07x faster                                                |
| nbody                    | 93.1 ms                                                | 87.4 ms: 1.07x faster                                                |
| nqueens                  | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                 |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                |
| logging_format           | 6.68 us                                                | 6.41 us: 1.04x faster                                                |
| pickle_pure_python       | 306 us                                                 | 295 us: 1.04x faster                                                 |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                                 |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.03x faster                                                 |
| logging_simple           | 6.03 us                                                | 5.84 us: 1.03x faster                                                |
| json                     | 4.94 ms                                                | 4.80 ms: 1.03x faster                                                |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                               |
| scimark_monte_carlo      | 68.1 ms                                                | 66.8 ms: 1.02x faster                                                |
| tornado_http             | 96.3 ms                                                | 94.8 ms: 1.02x faster                                                |
| sqlglot_optimize         | 53.1 ms                                                | 52.3 ms: 1.01x faster                                                |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.98 ms: 1.01x faster                                                |
| fannkuch                 | 388 ms                                                 | 385 ms: 1.01x faster                                                 |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.01x faster                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.45 sec: 1.01x faster                                               |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| bench_thread_pool        | 819 us                                                 | 821 us: 1.00x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 709 ms: 1.01x slower                                                 |
| richards                 | 45.7 ms                                                | 46.3 ms: 1.01x slower                                                |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                                |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                                |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                               |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                 |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                 |
| regex_dna                | 204 ms                                                 | 209 ms: 1.02x slower                                                 |
| mdp                      | 2.62 sec                                               | 2.68 sec: 1.03x slower                                               |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                                |
| float                    | 77.2 ms                                                | 79.4 ms: 1.03x slower                                                |
| deepcopy                 | 342 us                                                 | 352 us: 1.03x slower                                                 |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                |
| dulwich_log              | 63.7 ms                                                | 65.8 ms: 1.03x slower                                                |
| tomli_loads              | 2.22 sec                                               | 2.32 sec: 1.04x slower                                               |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.71 ms: 1.05x slower                                                |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                                 |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                |
| scimark_fft              | 328 ms                                                 | 350 ms: 1.06x slower                                                 |
| unpickle                 | 13.7 us                                                | 14.6 us: 1.07x slower                                                |
| pyflate                  | 418 ms                                                 | 447 ms: 1.07x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                |
| xml_etree_process        | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                                |
| xml_etree_generate       | 76.2 ms                                                | 83.9 ms: 1.10x slower                                                |
| python_startup           | 8.52 ms                                                | 9.40 ms: 1.10x slower                                                |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                                |
| unpack_sequence          | 43.1 ns                                                | 48.5 ns: 1.13x slower                                                |
| python_startup_no_site   | 6.01 ms                                                | 6.87 ms: 1.14x slower                                                |
| telco                    | 6.58 ms                                                | 7.83 ms: 1.19x slower                                                |
| async_generators         | 368 ms                                                 | 450 ms: 1.22x slower                                                 |
| dask                     | 360 ms                                                 | 515 ms: 1.43x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (3): meteor_contest, bench_mp_pool, unpickle_list
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 93.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
