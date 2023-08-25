
# Results vs. 3.11.0

- fork: python
- ref: af5cf1e75136fcef967d
- machine: linux-x86_64
- commit hash: af5cf1e
- commit date: 2023-07-11
- overall geometric mean: 1.04x faster
- HPT reliability: 74.05%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.76 ms: 1.06x faster                                                 |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                 |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.69 ms: 1.30x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 291 us: 1.05x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                  |
| json_loads           | 26.5 us                                                | 26.0 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                                 |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                 |
| tomli_loads          | 2.22 sec                                               | 2.28 sec: 1.03x slower                                                |
| unpickle_list        | 4.91 us                                                | 5.17 us: 1.05x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 57.2 ms: 1.06x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.40 us: 1.07x slower                                                 |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.18 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.35x faster                                                  |
| generators               | 73.5 ms                                                | 28.1 ms: 2.61x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.69 ms: 1.30x faster                                                 |
| mypy2                    | 420 ms                                                 | 334 ms: 1.26x faster                                                  |
| chaos                    | 69.2 ms                                                | 59.5 ms: 1.16x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.26 ms: 1.13x faster                                                 |
| raytrace                 | 297 ms                                                 | 268 ms: 1.11x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.18 sec: 1.10x faster                                                |
| async_tree_none          | 526 ms                                                 | 479 ms: 1.10x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.10x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                                  |
| async_tree_memoization   | 627 ms                                                 | 580 ms: 1.08x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                                 |
| crypto_pyaes             | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                 |
| richards_super           | 56.8 ms                                                | 53.4 ms: 1.06x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.76 ms: 1.06x faster                                                 |
| coverage                 | 100 ms                                                 | 94.4 ms: 1.06x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.04 ms: 1.06x faster                                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                                 |
| nqueens                  | 83.4 ms                                                | 79.2 ms: 1.05x faster                                                 |
| pickle_pure_python       | 306 us                                                 | 291 us: 1.05x faster                                                  |
| nbody                    | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 718 ms: 1.03x faster                                                  |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                 |
| logging_format           | 6.68 us                                                | 6.52 us: 1.03x faster                                                 |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| regex_compile            | 138 ms                                                 | 135 ms: 1.02x faster                                                  |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                  |
| json_loads               | 26.5 us                                                | 26.0 us: 1.02x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                |
| logging_silent           | 101 ns                                                 | 99.2 ns: 1.02x faster                                                 |
| json                     | 4.94 ms                                                | 4.88 ms: 1.01x faster                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 67.3 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                 |
| bench_thread_pool        | 819 us                                                 | 817 us: 1.00x faster                                                  |
| deepcopy_memo            | 37.0 us                                                | 37.2 us: 1.00x slower                                                 |
| pickle_dict              | 31.1 us                                                | 31.4 us: 1.01x slower                                                 |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                  |
| gc_traversal             | 4.02 ms                                                | 4.06 ms: 1.01x slower                                                 |
| mdp                      | 2.62 sec                                               | 2.64 sec: 1.01x slower                                                |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                  |
| pickle                   | 10.1 us                                                | 10.3 us: 1.02x slower                                                 |
| deepcopy                 | 342 us                                                 | 349 us: 1.02x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 717 ms: 1.02x slower                                                  |
| tomli_loads              | 2.22 sec                                               | 2.28 sec: 1.03x slower                                                |
| richards                 | 45.7 ms                                                | 47.0 ms: 1.03x slower                                                 |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                 |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 66.0 ms: 1.04x slower                                                 |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |
| regex_dna                | 204 ms                                                 | 214 ms: 1.05x slower                                                  |
| unpickle_list            | 4.91 us                                                | 5.17 us: 1.05x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 57.2 ms: 1.06x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                 |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                                  |
| pickle_list              | 4.11 us                                                | 4.40 us: 1.07x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.18 ms: 1.08x slower                                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.86 ms: 1.08x slower                                                 |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                 |
| scimark_fft              | 328 ms                                                 | 360 ms: 1.10x slower                                                  |
| spectral_norm            | 100 ms                                                 | 110 ms: 1.10x slower                                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.68 ms: 1.11x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.81 us: 1.11x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 48.3 ns: 1.12x slower                                                 |
| telco                    | 6.58 ms                                                | 7.40 ms: 1.12x slower                                                 |
| async_generators         | 368 ms                                                 | 443 ms: 1.20x slower                                                  |
| dask                     | 360 ms                                                 | 515 ms: 1.43x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, meteor_contest, bench_mp_pool, fannkuch
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 74.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
