
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: d87d67b
- commit date: 2023-07-23
- overall geometric mean: 1.03x faster
- HPT reliability: 53.75%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 100 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.8 ms: 1.06x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| float          | 77.2 ms                                                | 78.8 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.58 ms: 1.11x faster                                  |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.04x slower                                  |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                   |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                  |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                   |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| tomli_loads          | 2.22 sec                                               | 2.20 sec: 1.01x faster                                 |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                   |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.14 us: 1.05x slower                                  |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 58.7 ms: 1.09x slower                                  |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.8 ms: 1.11x slower                                  |
| pickle_list          | 4.11 us                                                | 4.69 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.30 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.75 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 149 us: 3.27x faster                                   |
| generators               | 73.5 ms                                                | 30.3 ms: 2.43x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                  |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                   |
| richards_super           | 56.8 ms                                                | 49.2 ms: 1.15x faster                                  |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.14x faster                                  |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                 |
| async_tree_none          | 526 ms                                                 | 472 ms: 1.12x faster                                   |
| regex_effbot             | 3.99 ms                                                | 3.58 ms: 1.11x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                   |
| chaos                    | 69.2 ms                                                | 63.6 ms: 1.09x faster                                  |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                  |
| coverage                 | 100 ms                                                 | 93.6 ms: 1.07x faster                                  |
| richards                 | 45.7 ms                                                | 42.8 ms: 1.07x faster                                  |
| nbody                    | 93.1 ms                                                | 87.8 ms: 1.06x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 216 us: 1.06x faster                                   |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                  |
| deltablue                | 3.67 ms                                                | 3.50 ms: 1.05x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.08 ms: 1.05x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                   |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 711 ms: 1.04x faster                                   |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                  |
| nqueens                  | 83.4 ms                                                | 81.1 ms: 1.03x faster                                  |
| json_loads               | 26.5 us                                                | 25.8 us: 1.03x faster                                  |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.03x faster                                   |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                 |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                 |
| logging_silent           | 101 ns                                                 | 99.1 ns: 1.02x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.96 ms: 1.01x faster                                  |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| tomli_loads              | 2.22 sec                                               | 2.20 sec: 1.01x faster                                 |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.00x faster                                   |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| fannkuch                 | 388 ms                                                 | 390 ms: 1.00x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 53.6 ms: 1.01x slower                                  |
| bench_thread_pool        | 819 us                                                 | 828 us: 1.01x slower                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| pickle_pure_python       | 306 us                                                 | 311 us: 1.02x slower                                   |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                  |
| float                    | 77.2 ms                                                | 78.8 ms: 1.02x slower                                  |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.3 ms: 1.02x slower                                  |
| pickle_dict              | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| logging_format           | 6.68 us                                                | 6.85 us: 1.03x slower                                  |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                 |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                   |
| 2to3                     | 259 ms                                                 | 267 ms: 1.03x slower                                   |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| crypto_pyaes             | 74.7 ms                                                | 77.1 ms: 1.03x slower                                  |
| regex_v8                 | 22.0 ms                                                | 22.8 ms: 1.04x slower                                  |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                   |
| telco                    | 6.58 ms                                                | 6.84 ms: 1.04x slower                                  |
| tornado_http             | 96.3 ms                                                | 100 ms: 1.04x slower                                   |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| logging_simple           | 6.03 us                                                | 6.27 us: 1.04x slower                                  |
| regex_dna                | 204 ms                                                 | 213 ms: 1.04x slower                                   |
| regex_compile            | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                   |
| unpickle_list            | 4.91 us                                                | 5.14 us: 1.05x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 736 ms: 1.05x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 71.7 ms: 1.05x slower                                  |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                  |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                  |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                   |
| dulwich_log              | 63.7 ms                                                | 67.8 ms: 1.06x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.90 ms: 1.09x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 58.7 ms: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.30 ms: 1.09x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                  |
| scimark_fft              | 328 ms                                                 | 362 ms: 1.10x slower                                   |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.11x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 84.8 ms: 1.11x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.75 ms: 1.12x slower                                  |
| pickle_list              | 4.11 us                                                | 4.69 us: 1.14x slower                                  |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                   |
| unpack_sequence          | 43.1 ns                                                | 52.7 ns: 1.22x slower                                  |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (5): pathlib, sqlglot_normalize, raytrace, bench_mp_pool, json
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 53.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
