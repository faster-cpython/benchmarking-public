
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 266 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| tornado_http   | 96.3 ms                                                | 98.6 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.5 ms: 1.04x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| float          | 77.2 ms                                                | 79.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.72 ms: 1.07x faster                                  |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                   |
| regex_v8       | 22.0 ms                                                | 22.6 ms: 1.03x slower                                  |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.87 ms: 1.27x faster                                  |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.05x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                   |
| json_loads           | 26.5 us                                                | 25.9 us: 1.02x faster                                  |
| tomli_loads          | 2.22 sec                                               | 2.19 sec: 1.01x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                   |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                  |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.9 ms: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 85.7 ms: 1.12x slower                                  |
| pickle_list          | 4.11 us                                                | 4.70 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.26 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.73 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-linux-x86_64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.36x faster                                   |
| generators               | 73.5 ms                                                | 30.4 ms: 2.41x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.87 ms: 1.27x faster                                  |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                   |
| richards_super           | 56.8 ms                                                | 49.9 ms: 1.14x faster                                  |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                  |
| async_tree_none          | 526 ms                                                 | 467 ms: 1.13x faster                                   |
| async_tree_io            | 1.30 sec                                               | 1.15 sec: 1.12x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 569 ms: 1.10x faster                                   |
| chaos                    | 69.2 ms                                                | 63.4 ms: 1.09x faster                                  |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                  |
| regex_effbot             | 3.99 ms                                                | 3.72 ms: 1.07x faster                                  |
| coverage                 | 100 ms                                                 | 94.2 ms: 1.06x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.05x faster                                   |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 707 ms: 1.05x faster                                   |
| deltablue                | 3.67 ms                                                | 3.51 ms: 1.04x faster                                  |
| nbody                    | 93.1 ms                                                | 89.5 ms: 1.04x faster                                  |
| richards                 | 45.7 ms                                                | 44.1 ms: 1.04x faster                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                   |
| logging_silent           | 101 ns                                                 | 97.9 ns: 1.03x faster                                  |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| nqueens                  | 83.4 ms                                                | 80.9 ms: 1.03x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.19 ms: 1.03x faster                                  |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.02x faster                                   |
| json_loads               | 26.5 us                                                | 25.9 us: 1.02x faster                                  |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                 |
| tomli_loads              | 2.22 sec                                               | 2.19 sec: 1.01x faster                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| mdp                      | 2.62 sec                                               | 2.59 sec: 1.01x faster                                 |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| bench_thread_pool        | 819 us                                                 | 827 us: 1.01x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                 |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                  |
| sqlglot_optimize         | 53.1 ms                                                | 53.8 ms: 1.01x slower                                  |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| fannkuch                 | 388 ms                                                 | 393 ms: 1.01x slower                                   |
| pickle_pure_python       | 306 us                                                 | 311 us: 1.02x slower                                   |
| json                     | 4.94 ms                                                | 5.04 ms: 1.02x slower                                  |
| regex_dna                | 204 ms                                                 | 209 ms: 1.02x slower                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.3 ms: 1.02x slower                                  |
| tornado_http             | 96.3 ms                                                | 98.6 ms: 1.02x slower                                  |
| regex_v8                 | 22.0 ms                                                | 22.6 ms: 1.03x slower                                  |
| crypto_pyaes             | 74.7 ms                                                | 76.7 ms: 1.03x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 721 ms: 1.03x slower                                   |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.03x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                  |
| spectral_norm            | 100 ms                                                 | 103 ms: 1.03x slower                                   |
| 2to3                     | 259 ms                                                 | 266 ms: 1.03x slower                                   |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                   |
| float                    | 77.2 ms                                                | 79.8 ms: 1.03x slower                                  |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                   |
| docutils                 | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| regex_compile            | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| logging_simple           | 6.03 us                                                | 6.29 us: 1.04x slower                                  |
| telco                    | 6.58 ms                                                | 6.88 ms: 1.05x slower                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| logging_format           | 6.68 us                                                | 7.00 us: 1.05x slower                                  |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 71.8 ms: 1.05x slower                                  |
| dulwich_log              | 63.7 ms                                                | 67.7 ms: 1.06x slower                                  |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                   |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                  |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                  |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                  |
| python_startup           | 8.52 ms                                                | 9.26 ms: 1.09x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                  |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                   |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.95 ms: 1.10x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 59.9 ms: 1.11x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.73 ms: 1.12x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 85.7 ms: 1.12x slower                                  |
| pickle_list              | 4.11 us                                                | 4.70 us: 1.14x slower                                  |
| async_generators         | 368 ms                                                 | 442 ms: 1.20x slower                                   |
| unpack_sequence          | 43.1 ns                                                | 53.9 ns: 1.25x slower                                  |
| dask                     | 360 ms                                                 | 534 ms: 1.48x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): pickle_dict, bench_mp_pool, raytrace, unpickle_list
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
