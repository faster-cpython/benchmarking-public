
# Results vs. 3.11.0

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.00x faster \*
- HPT reliability: 87.12%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 258 ms: 1.00x faster                                   |
| chameleon      | 6.47 ms                                                | 6.63 ms: 1.02x slower                                  |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                 |
| html5lib       | 64.5 ms                                                | 63.4 ms: 1.02x faster                                  |
| tornado_http   | 96.3 ms                                                | 99.8 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 77.2 ms                                                | 76.0 ms: 1.02x faster                                  |
| nbody          | 93.1 ms                                                | 95.4 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.31 ms: 1.21x faster                                  |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|---------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads          | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| pickle              | 10.1 us                                                | 9.72 us: 1.04x faster                                  |
| xml_etree_iterparse | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| xml_etree_generate  | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| unpickle_list       | 4.91 us                                                | 4.95 us: 1.01x slower                                  |
| pickle_pure_python  | 306 us                                                 | 310 us: 1.01x slower                                   |
| pickle_list         | 4.11 us                                                | 4.17 us: 1.01x slower                                  |
| Geometric mean      | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (6): unpickle, xml_etree_parse, xml_etree_process, pickle_dict, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.98 ms: 1.00x faster                                  |
| python_startup         | 8.52 ms                                                | 8.49 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.92 ms: 1.02x faster                                  |
| genshi_xml      | 51.8 ms                                                | 52.5 ms: 1.01x slower                                  |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                  |
| genshi_text     | 21.6 ms                                                | 22.1 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.31 ms: 1.21x faster                                  |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.05 ms: 1.05x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.13 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| pickle                  | 10.1 us                                                | 9.72 us: 1.04x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 889 ms: 1.04x faster                                   |
| async_generators        | 368 ms                                                 | 358 ms: 1.03x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 72.6 ms: 1.03x faster                                  |
| docutils                | 2.63 sec                                               | 2.57 sec: 1.02x faster                                 |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                   |
| logging_format          | 6.68 us                                                | 6.54 us: 1.02x faster                                  |
| sqlite_synth            | 2.52 us                                                | 2.47 us: 1.02x faster                                  |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| scimark_sor             | 118 ms                                                 | 116 ms: 1.02x faster                                   |
| html5lib                | 64.5 ms                                                | 63.4 ms: 1.02x faster                                  |
| mako                    | 10.1 ms                                                | 9.92 ms: 1.02x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.38 ms: 1.02x faster                                  |
| float                   | 77.2 ms                                                | 76.0 ms: 1.02x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.02x faster                                  |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.01x faster                                 |
| logging_simple          | 6.03 us                                                | 5.95 us: 1.01x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.44 sec: 1.01x faster                                 |
| fannkuch                | 388 ms                                                 | 384 ms: 1.01x faster                                   |
| raytrace                | 297 ms                                                 | 294 ms: 1.01x faster                                   |
| coroutines              | 25.5 ms                                                | 25.3 ms: 1.01x faster                                  |
| bench_thread_pool       | 819 us                                                 | 813 us: 1.01x faster                                   |
| regex_compile           | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                  |
| pyflate                 | 418 ms                                                 | 415 ms: 1.01x faster                                   |
| flaskblogging           | 7.12 ms                                                | 7.07 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| sympy_expand            | 475 ms                                                 | 472 ms: 1.01x faster                                   |
| python_startup_no_site  | 6.01 ms                                                | 5.98 ms: 1.00x faster                                  |
| python_startup          | 8.52 ms                                                | 8.49 ms: 1.00x faster                                  |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.00x faster                                   |
| generators              | 73.5 ms                                                | 73.3 ms: 1.00x faster                                  |
| 2to3                    | 259 ms                                                 | 258 ms: 1.00x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 53.3 ms: 1.00x slower                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 742 ms: 1.00x slower                                   |
| deepcopy_memo           | 37.0 us                                                | 37.2 us: 1.00x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.01x slower                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 68.4 ms: 1.01x slower                                  |
| chaos                   | 69.2 ms                                                | 69.6 ms: 1.01x slower                                  |
| mdp                     | 2.62 sec                                               | 2.64 sec: 1.01x slower                                 |
| unpickle_list           | 4.91 us                                                | 4.95 us: 1.01x slower                                  |
| logging_silent          | 101 ns                                                 | 102 ns: 1.01x slower                                   |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| telco                   | 6.58 ms                                                | 6.66 ms: 1.01x slower                                  |
| thrift                  | 756 us                                                 | 765 us: 1.01x slower                                   |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                  |
| pickle_pure_python      | 306 us                                                 | 310 us: 1.01x slower                                   |
| hexiom                  | 6.37 ms                                                | 6.46 ms: 1.01x slower                                  |
| pickle_list             | 4.11 us                                                | 4.17 us: 1.01x slower                                  |
| spectral_norm           | 100 ms                                                 | 101 ms: 1.01x slower                                   |
| genshi_xml              | 51.8 ms                                                | 52.5 ms: 1.01x slower                                  |
| dask                    | 360 ms                                                 | 365 ms: 1.01x slower                                   |
| nqueens                 | 83.4 ms                                                | 85.0 ms: 1.02x slower                                  |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                  |
| deepcopy                | 342 us                                                 | 349 us: 1.02x slower                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.59 ms: 1.02x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 141 ms: 1.02x slower                                   |
| chameleon               | 6.47 ms                                                | 6.63 ms: 1.02x slower                                  |
| nbody                   | 93.1 ms                                                | 95.4 ms: 1.02x slower                                  |
| richards                | 45.7 ms                                                | 46.9 ms: 1.03x slower                                  |
| genshi_text             | 21.6 ms                                                | 22.1 ms: 1.03x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 44.6 ns: 1.04x slower                                  |
| tornado_http            | 96.3 ms                                                | 99.8 ms: 1.04x slower                                  |
| coverage                | 100 ms                                                 | 104 ms: 1.04x slower                                   |
| deepcopy_reduce         | 2.94 us                                                | 3.09 us: 1.05x slower                                  |
| gc_traversal            | 4.02 ms                                                | 4.26 ms: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (22): unpickle, pylint, meteor_contest, async_tree_none, xml_etree_parse, sympy_str, create_gc_cycles, scimark_fft, dulwich_log, pprint_safe_repr, xml_etree_process, go, pickle_dict, deltablue, bench_mp_pool, async_tree_memoization, sympy_integrate, mypy2, json_dumps, unpickle_pure_python, sqlalchemy_imperative, djangocms
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 87.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
