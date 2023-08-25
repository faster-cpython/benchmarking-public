
# Results vs. 3.11.0

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: 19b61a7
- commit date: 2023-02-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                 |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                               |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                |
| tornado_http   | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.5 ms: 1.05x faster                                                |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.27 ms: 1.22x faster                                                |
| regex_compile  | 138 ms                                                 | 133 ms: 1.03x faster                                                 |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.34 ms: 1.35x faster                                                |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                                 |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 98.5 ms: 1.05x faster                                                |
| pickle_list          | 4.11 us                                                | 3.92 us: 1.05x faster                                                |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                                 |
| pickle_dict          | 31.1 us                                                | 30.1 us: 1.03x faster                                                |
| pickle               | 10.1 us                                                | 9.95 us: 1.01x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 55.8 ms: 1.04x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 81.5 ms: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.1 ms: 1.08x faster                                                |
| mako            | 10.1 ms                                                | 9.93 ms: 1.02x faster                                                |
| django_template | 32.6 ms                                                | 33.5 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators             | 73.5 ms                                                | 30.5 ms: 2.41x faster                                                |
| asyncio_tcp            | 922 ms                                                 | 505 ms: 1.82x faster                                                 |
| json_dumps             | 12.6 ms                                                | 9.34 ms: 1.35x faster                                                |
| mypy2                  | 420 ms                                                 | 334 ms: 1.26x faster                                                 |
| regex_effbot           | 3.99 ms                                                | 3.27 ms: 1.22x faster                                                |
| coroutines             | 25.5 ms                                                | 22.3 ms: 1.14x faster                                                |
| deltablue              | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                |
| unpickle_pure_python   | 228 us                                                 | 203 us: 1.12x faster                                                 |
| json_loads             | 26.5 us                                                | 23.8 us: 1.11x faster                                                |
| aiohttp                | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                |
| json                   | 4.94 ms                                                | 4.55 ms: 1.09x faster                                                |
| scimark_sor            | 118 ms                                                 | 109 ms: 1.08x faster                                                 |
| genshi_xml             | 51.8 ms                                                | 48.1 ms: 1.08x faster                                                |
| gunicorn               | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                |
| xml_etree_parse        | 158 ms                                                 | 148 ms: 1.07x faster                                                 |
| logging_silent         | 101 ns                                                 | 95.4 ns: 1.06x faster                                                |
| fannkuch               | 388 ms                                                 | 367 ms: 1.06x faster                                                 |
| pycparser              | 1.18 sec                                               | 1.12 sec: 1.06x faster                                               |
| xml_etree_iterparse    | 104 ms                                                 | 98.5 ms: 1.05x faster                                                |
| richards               | 45.7 ms                                                | 43.4 ms: 1.05x faster                                                |
| float                  | 77.2 ms                                                | 73.5 ms: 1.05x faster                                                |
| scimark_fft            | 328 ms                                                 | 312 ms: 1.05x faster                                                 |
| pickle_list            | 4.11 us                                                | 3.92 us: 1.05x faster                                                |
| spectral_norm          | 100 ms                                                 | 95.9 ms: 1.04x faster                                                |
| pickle_pure_python     | 306 us                                                 | 293 us: 1.04x faster                                                 |
| coverage               | 100 ms                                                 | 95.9 ms: 1.04x faster                                                |
| deepcopy_memo          | 37.0 us                                                | 35.6 us: 1.04x faster                                                |
| sqlglot_optimize       | 53.1 ms                                                | 51.2 ms: 1.04x faster                                                |
| pprint_pformat         | 1.46 sec                                               | 1.41 sec: 1.04x faster                                               |
| pickle_dict            | 31.1 us                                                | 30.1 us: 1.03x faster                                                |
| regex_compile          | 138 ms                                                 | 133 ms: 1.03x faster                                                 |
| html5lib               | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                |
| pathlib                | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                |
| mdp                    | 2.62 sec                                               | 2.53 sec: 1.03x faster                                               |
| 2to3                   | 259 ms                                                 | 251 ms: 1.03x faster                                                 |
| meteor_contest         | 107 ms                                                 | 103 ms: 1.03x faster                                                 |
| bench_thread_pool      | 819 us                                                 | 794 us: 1.03x faster                                                 |
| docutils               | 2.63 sec                                               | 2.55 sec: 1.03x faster                                               |
| scimark_monte_carlo    | 68.1 ms                                                | 66.2 ms: 1.03x faster                                                |
| pidigits               | 198 ms                                                 | 193 ms: 1.03x faster                                                 |
| go                     | 140 ms                                                 | 136 ms: 1.03x faster                                                 |
| unpack_sequence        | 43.1 ns                                                | 41.9 ns: 1.03x faster                                                |
| sqlglot_normalize      | 108 ms                                                 | 105 ms: 1.03x faster                                                 |
| raytrace               | 297 ms                                                 | 289 ms: 1.03x faster                                                 |
| logging_format         | 6.68 us                                                | 6.51 us: 1.03x faster                                                |
| telco                  | 6.58 ms                                                | 6.42 ms: 1.03x faster                                                |
| hexiom                 | 6.37 ms                                                | 6.22 ms: 1.02x faster                                                |
| pprint_safe_repr       | 701 ms                                                 | 686 ms: 1.02x faster                                                 |
| nqueens                | 83.4 ms                                                | 81.6 ms: 1.02x faster                                                |
| sympy_expand           | 475 ms                                                 | 465 ms: 1.02x faster                                                 |
| pyflate                | 418 ms                                                 | 411 ms: 1.02x faster                                                 |
| logging_simple         | 6.03 us                                                | 5.93 us: 1.02x faster                                                |
| mako                   | 10.1 ms                                                | 9.93 ms: 1.02x faster                                                |
| create_gc_cycles       | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                |
| pickle                 | 10.1 us                                                | 9.95 us: 1.01x faster                                                |
| crypto_pyaes           | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                |
| sympy_integrate        | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                |
| sympy_str              | 290 ms                                                 | 287 ms: 1.01x faster                                                 |
| chaos                  | 69.2 ms                                                | 68.5 ms: 1.01x faster                                                |
| tornado_http           | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                |
| sqlalchemy_declarative | 138 ms                                                 | 137 ms: 1.01x faster                                                 |
| dulwich_log            | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                |
| deepcopy               | 342 us                                                 | 341 us: 1.00x faster                                                 |
| sympy_sum              | 167 ms                                                 | 168 ms: 1.01x slower                                                 |
| gc_traversal           | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                |
| sqlalchemy_imperative  | 17.9 ms                                                | 18.2 ms: 1.02x slower                                                |
| sqlglot_transpile      | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                |
| django_template        | 32.6 ms                                                | 33.5 ms: 1.03x slower                                                |
| thrift                 | 756 us                                                 | 779 us: 1.03x slower                                                 |
| sqlglot_parse          | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                |
| regex_dna              | 204 ms                                                 | 210 ms: 1.03x slower                                                 |
| sqlite_synth           | 2.52 us                                                | 2.60 us: 1.03x slower                                                |
| xml_etree_process      | 53.9 ms                                                | 55.8 ms: 1.04x slower                                                |
| deepcopy_reduce        | 2.94 us                                                | 3.08 us: 1.05x slower                                                |
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                                |
| async_tree_memoization | 627 ms                                                 | 662 ms: 1.05x slower                                                 |
| xml_etree_generate     | 76.2 ms                                                | 81.5 ms: 1.07x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                |
| async_generators       | 368 ms                                                 | 411 ms: 1.12x slower                                                 |
| dask                   | 360 ms                                                 | 509 ms: 1.41x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (13): async_tree_none, unpickle, async_tree_io, genshi_text, async_tree_cpu_io_mixed, bench_mp_pool, unpickle_list, chameleon, scimark_sparse_mat_mult, scimark_lu, regex_v8, djangocms, nbody
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
