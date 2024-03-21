# Results vs. base

- fork: faster-cpython
- ref: fix_gc_counting
- machine: linux-x86_64
- commit hash: d0672a4
- commit date: 2024-03-21
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                 | 268 ms: 1.10x faster                                                        |
| docutils       | 4.66 sec                                                               | 2.74 sec: 1.70x faster                                                      |
| html5lib       | 75.1 ms                                                                | 65.4 ms: 1.15x faster                                                       |
| tornado_http   | 99.0 ms                                                                | 94.8 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.18x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 14.3 sec                                                               | 917 ms: 15.54x faster                                                       |
| async_tree_io              | 13.3 sec                                                               | 917 ms: 14.48x faster                                                       |
| async_tree_none_tg         | 3.77 sec                                                               | 350 ms: 10.79x faster                                                       |
| async_tree_memoization_tg  | 4.73 sec                                                               | 442 ms: 10.70x faster                                                       |
| async_tree_memoization     | 4.45 sec                                                               | 461 ms: 9.65x faster                                                        |
| async_tree_none            | 3.44 sec                                                               | 374 ms: 9.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 4.57 sec                                                               | 606 ms: 7.54x faster                                                        |
| async_tree_cpu_io_mixed    | 4.17 sec                                                               | 590 ms: 7.06x faster                                                        |
| Geometric mean             | (ref)                                                                  | 10.26x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 145 ms                                                                 | 78.5 ms: 1.85x faster                                                       |
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x faster                                                        |
| nbody          | 89.1 ms                                                                | 89.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                 | 135 ms: 1.00x slower                                                        |
| regex_effbot   | 3.59 ms                                                                | 3.61 ms: 1.01x slower                                                       |
| regex_dna      | 214 ms                                                                 | 218 ms: 1.02x slower                                                        |
| regex_v8       | 24.4 ms                                                                | 24.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse | 167 ms                                                                 | 107 ms: 1.56x faster                                                        |
| xml_etree_parse     | 220 ms                                                                 | 162 ms: 1.36x faster                                                        |
| xml_etree_generate  | 98.8 ms                                                                | 85.5 ms: 1.15x faster                                                       |
| xml_etree_process   | 68.6 ms                                                                | 59.8 ms: 1.15x faster                                                       |
| unpickle            | 15.6 us                                                                | 14.6 us: 1.07x faster                                                       |
| pickle_dict         | 36.5 us                                                                | 35.3 us: 1.03x faster                                                       |
| pickle              | 12.1 us                                                                | 11.8 us: 1.03x faster                                                       |
| json_dumps          | 10.6 ms                                                                | 10.4 ms: 1.02x faster                                                       |
| unpickle_list       | 5.20 us                                                                | 5.24 us: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (5): pickle_list, tomli_loads, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 10.5 ms                                                                | 10.4 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                                | 52.1 ms: 1.16x faster                                                       |
| django_template | 34.3 ms                                                                | 34.0 ms: 1.01x faster                                                       |
| genshi_text     | 23.2 ms                                                                | 23.1 ms: 1.00x faster                                                       |
| mako            | 11.1 ms                                                                | 11.5 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5+-6547330 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 14.3 sec                                                               | 917 ms: 15.54x faster                                                       |
| async_tree_io              | 13.3 sec                                                               | 917 ms: 14.48x faster                                                       |
| async_tree_none_tg         | 3.77 sec                                                               | 350 ms: 10.79x faster                                                       |
| async_tree_memoization_tg  | 4.73 sec                                                               | 442 ms: 10.70x faster                                                       |
| async_tree_memoization     | 4.45 sec                                                               | 461 ms: 9.65x faster                                                        |
| async_tree_none            | 3.44 sec                                                               | 374 ms: 9.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 4.57 sec                                                               | 606 ms: 7.54x faster                                                        |
| async_tree_cpu_io_mixed    | 4.17 sec                                                               | 590 ms: 7.06x faster                                                        |
| pylint                     | 1.00 sec                                                               | 317 ms: 3.15x faster                                                        |
| dask                       | 755 ms                                                                 | 368 ms: 2.05x faster                                                        |
| float                      | 145 ms                                                                 | 78.5 ms: 1.85x faster                                                       |
| docutils                   | 4.66 sec                                                               | 2.74 sec: 1.70x faster                                                      |
| xml_etree_iterparse        | 167 ms                                                                 | 107 ms: 1.56x faster                                                        |
| xml_etree_parse            | 220 ms                                                                 | 162 ms: 1.36x faster                                                        |
| pycparser                  | 1.46 sec                                                               | 1.17 sec: 1.25x faster                                                      |
| async_generators           | 538 ms                                                                 | 440 ms: 1.22x faster                                                        |
| sqlglot_transpile          | 1.86 ms                                                                | 1.58 ms: 1.18x faster                                                       |
| sqlglot_parse              | 1.50 ms                                                                | 1.28 ms: 1.17x faster                                                       |
| genshi_xml                 | 60.6 ms                                                                | 52.1 ms: 1.16x faster                                                       |
| xml_etree_generate         | 98.8 ms                                                                | 85.5 ms: 1.15x faster                                                       |
| html5lib                   | 75.1 ms                                                                | 65.4 ms: 1.15x faster                                                       |
| xml_etree_process          | 68.6 ms                                                                | 59.8 ms: 1.15x faster                                                       |
| deltablue                  | 3.67 ms                                                                | 3.28 ms: 1.12x faster                                                       |
| 2to3                       | 296 ms                                                                 | 268 ms: 1.10x faster                                                        |
| mypy2                      | 810 ms                                                                 | 738 ms: 1.10x faster                                                        |
| unpack_sequence            | 47.8 ns                                                                | 44.2 ns: 1.08x faster                                                       |
| unpickle                   | 15.6 us                                                                | 14.6 us: 1.07x faster                                                       |
| djangocms                  | 33.0 us                                                                | 31.3 us: 1.05x faster                                                       |
| mdp                        | 2.85 sec                                                               | 2.71 sec: 1.05x faster                                                      |
| aiohttp                    | 1.23 ms                                                                | 1.17 ms: 1.05x faster                                                       |
| gunicorn                   | 1.32 ms                                                                | 1.27 ms: 1.04x faster                                                       |
| tornado_http               | 99.0 ms                                                                | 94.8 ms: 1.04x faster                                                       |
| create_gc_cycles           | 1.49 ms                                                                | 1.44 ms: 1.04x faster                                                       |
| pickle_dict                | 36.5 us                                                                | 35.3 us: 1.03x faster                                                       |
| sqlglot_optimize           | 56.5 ms                                                                | 54.8 ms: 1.03x faster                                                       |
| pickle                     | 12.1 us                                                                | 11.8 us: 1.03x faster                                                       |
| typing_runtime_protocols   | 116 us                                                                 | 113 us: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.92 ms                                                                | 4.81 ms: 1.02x faster                                                       |
| pathlib                    | 18.8 ms                                                                | 18.4 ms: 1.02x faster                                                       |
| richards                   | 47.2 ms                                                                | 46.1 ms: 1.02x faster                                                       |
| comprehensions             | 16.7 us                                                                | 16.4 us: 1.02x faster                                                       |
| json_dumps                 | 10.6 ms                                                                | 10.4 ms: 1.02x faster                                                       |
| gc_traversal               | 3.71 ms                                                                | 3.65 ms: 1.02x faster                                                       |
| richards_super             | 53.8 ms                                                                | 53.1 ms: 1.01x faster                                                       |
| scimark_fft                | 364 ms                                                                 | 360 ms: 1.01x faster                                                        |
| logging_simple             | 5.91 us                                                                | 5.84 us: 1.01x faster                                                       |
| python_startup             | 10.5 ms                                                                | 10.4 ms: 1.01x faster                                                       |
| dulwich_log                | 68.5 ms                                                                | 67.9 ms: 1.01x faster                                                       |
| scimark_lu                 | 114 ms                                                                 | 113 ms: 1.01x faster                                                        |
| django_template            | 34.3 ms                                                                | 34.0 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.91 us                                                                | 2.89 us: 1.01x faster                                                       |
| pprint_pformat             | 1.52 sec                                                               | 1.51 sec: 1.01x faster                                                      |
| pprint_safe_repr           | 746 ms                                                                 | 741 ms: 1.01x faster                                                        |
| sympy_expand               | 466 ms                                                                 | 463 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 108 ms                                                                 | 108 ms: 1.01x faster                                                        |
| genshi_text                | 23.2 ms                                                                | 23.1 ms: 1.00x faster                                                       |
| pidigits                   | 190 ms                                                                 | 190 ms: 1.00x faster                                                        |
| sympy_integrate            | 20.1 ms                                                                | 20.0 ms: 1.00x faster                                                       |
| regex_compile              | 135 ms                                                                 | 135 ms: 1.00x slower                                                        |
| spectral_norm              | 114 ms                                                                 | 114 ms: 1.00x slower                                                        |
| crypto_pyaes               | 72.6 ms                                                                | 72.9 ms: 1.00x slower                                                       |
| asyncio_tcp                | 500 ms                                                                 | 503 ms: 1.01x slower                                                        |
| meteor_contest             | 110 ms                                                                 | 110 ms: 1.01x slower                                                        |
| regex_effbot               | 3.59 ms                                                                | 3.61 ms: 1.01x slower                                                       |
| unpickle_list              | 5.20 us                                                                | 5.24 us: 1.01x slower                                                       |
| nbody                      | 89.1 ms                                                                | 89.9 ms: 1.01x slower                                                       |
| deepcopy                   | 349 us                                                                 | 353 us: 1.01x slower                                                        |
| hexiom                     | 6.27 ms                                                                | 6.34 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 68.7 ms                                                                | 69.6 ms: 1.01x slower                                                       |
| fannkuch                   | 401 ms                                                                 | 406 ms: 1.01x slower                                                        |
| coroutines                 | 22.9 ms                                                                | 23.2 ms: 1.01x slower                                                       |
| regex_dna                  | 214 ms                                                                 | 218 ms: 1.02x slower                                                        |
| regex_v8                   | 24.4 ms                                                                | 24.8 ms: 1.02x slower                                                       |
| generators                 | 29.6 ms                                                                | 30.1 ms: 1.02x slower                                                       |
| json                       | 5.21 ms                                                                | 5.31 ms: 1.02x slower                                                       |
| pyflate                    | 470 ms                                                                 | 483 ms: 1.03x slower                                                        |
| mako                       | 11.1 ms                                                                | 11.5 ms: 1.04x slower                                                       |
| scimark_sor                | 123 ms                                                                 | 131 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.27x faster                                                                |

Benchmark hidden because not significant (24): bench_mp_pool, logging_silent, go, deepcopy_reduce, deepcopy_memo, raytrace, logging_format, nqueens, thrift, coverage, sympy_sum, asyncio_websockets, pickle_list, asyncio_tcp_ssl, tomli_loads, unpickle_pure_python, chaos, python_startup_no_site, bench_thread_pool, pickle_pure_python, chameleon, sympy_str, telco, json_loads


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.06x