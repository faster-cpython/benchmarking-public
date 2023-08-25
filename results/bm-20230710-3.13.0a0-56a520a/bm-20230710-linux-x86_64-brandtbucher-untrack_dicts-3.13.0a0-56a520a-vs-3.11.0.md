
# Results vs. 3.11.0

- fork: brandtbucher
- ref: untrack_dicts
- machine: linux-x86_64
- commit hash: 56a520a
- commit date: 2023-07-10
- overall geometric mean: 1.04x faster
- HPT reliability: 79.14%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                 |
| nbody          | 93.1 ms                                                | 94.1 ms: 1.01x slower                                                |
| float          | 77.2 ms                                                | 79.9 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.13x faster                                                |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                 |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.64 ms: 1.31x faster                                                |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                 |
| pickle_pure_python   | 306 us                                                 | 291 us: 1.05x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                 |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                                |
| tomli_loads          | 2.22 sec                                               | 2.28 sec: 1.03x slower                                               |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                                |
| pickle_list          | 4.11 us                                                | 4.39 us: 1.07x slower                                                |
| xml_etree_process    | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 85.7 ms: 1.12x slower                                                |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.21 ms: 1.08x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 150 us: 3.24x faster                                                 |
| generators               | 73.5 ms                                                | 28.4 ms: 2.59x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                 |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                               |
| json_dumps               | 12.6 ms                                                | 9.64 ms: 1.31x faster                                                |
| mypy2                    | 420 ms                                                 | 335 ms: 1.25x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.2 ms: 1.17x faster                                                |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.15x faster                                                |
| regex_effbot             | 3.99 ms                                                | 3.52 ms: 1.13x faster                                                |
| deltablue                | 3.67 ms                                                | 3.31 ms: 1.11x faster                                                |
| async_tree_io            | 1.30 sec                                               | 1.17 sec: 1.11x faster                                               |
| async_tree_none          | 526 ms                                                 | 478 ms: 1.10x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.10x faster                                                |
| raytrace                 | 297 ms                                                 | 272 ms: 1.09x faster                                                 |
| coverage                 | 100 ms                                                 | 92.0 ms: 1.09x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.08x faster                                                |
| async_tree_memoization   | 627 ms                                                 | 581 ms: 1.08x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                 |
| richards_super           | 56.8 ms                                                | 53.4 ms: 1.06x faster                                                |
| crypto_pyaes             | 74.7 ms                                                | 70.3 ms: 1.06x faster                                                |
| hexiom                   | 6.37 ms                                                | 6.01 ms: 1.06x faster                                                |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                |
| pickle_pure_python       | 306 us                                                 | 291 us: 1.05x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.91 ms: 1.03x faster                                                |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                               |
| logging_format           | 6.68 us                                                | 6.51 us: 1.03x faster                                                |
| json_loads               | 26.5 us                                                | 25.8 us: 1.03x faster                                                |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                 |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 722 ms: 1.02x faster                                                 |
| json                     | 4.94 ms                                                | 4.84 ms: 1.02x faster                                                |
| nqueens                  | 83.4 ms                                                | 81.7 ms: 1.02x faster                                                |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                 |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                 |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                |
| sqlglot_optimize         | 53.1 ms                                                | 52.8 ms: 1.01x faster                                                |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                 |
| nbody                    | 93.1 ms                                                | 94.1 ms: 1.01x slower                                                |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                               |
| fannkuch                 | 388 ms                                                 | 393 ms: 1.01x slower                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                               |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                                |
| pickle_dict              | 31.1 us                                                | 31.7 us: 1.02x slower                                                |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.02x slower                                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                                |
| richards                 | 45.7 ms                                                | 46.9 ms: 1.03x slower                                                |
| tomli_loads              | 2.22 sec                                               | 2.28 sec: 1.03x slower                                               |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 65.4 ms: 1.03x slower                                                |
| pprint_safe_repr         | 701 ms                                                 | 722 ms: 1.03x slower                                                 |
| pickle                   | 10.1 us                                                | 10.4 us: 1.03x slower                                                |
| float                    | 77.2 ms                                                | 79.9 ms: 1.03x slower                                                |
| unpack_sequence          | 43.1 ns                                                | 44.7 ns: 1.04x slower                                                |
| pathlib                  | 18.2 ms                                                | 18.9 ms: 1.04x slower                                                |
| regex_dna                | 204 ms                                                 | 213 ms: 1.04x slower                                                 |
| unpickle_list            | 4.91 us                                                | 5.12 us: 1.04x slower                                                |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.70 ms: 1.05x slower                                                |
| pyflate                  | 418 ms                                                 | 443 ms: 1.06x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.39 us: 1.07x slower                                                |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.21 ms: 1.08x slower                                                |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                |
| telco                    | 6.58 ms                                                | 7.15 ms: 1.09x slower                                                |
| xml_etree_process        | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                                |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                |
| python_startup_no_site   | 6.01 ms                                                | 6.71 ms: 1.12x slower                                                |
| xml_etree_generate       | 76.2 ms                                                | 85.7 ms: 1.12x slower                                                |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                                 |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (6): logging_silent, scimark_monte_carlo, tornado_http, bench_mp_pool, bench_thread_pool, pycparser
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 79.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
