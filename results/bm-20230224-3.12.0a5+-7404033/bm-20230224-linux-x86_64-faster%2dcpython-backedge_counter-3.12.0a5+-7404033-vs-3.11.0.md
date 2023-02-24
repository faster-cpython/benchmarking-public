
# Results vs. 3.11.0

- fork: faster-cpython
- ref: backedge_counter
- machine: linux-x86_64
- commit hash: 7404033
- commit date: 2023-02-24
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.48 ms: 1.02x slower                                                        |
| docutils       | 2.60 sec                                               | 2.65 sec: 1.02x slower                                                       |
| html5lib       | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                        |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                         |
| nbody          | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.27 ms: 1.06x faster                                                        |
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                         |
| regex_v8       | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                        |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.47 ms: 1.30x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                         |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 289 us: 1.07x faster                                                         |
| pickle_list          | 4.14 us                                                | 4.00 us: 1.03x faster                                                        |
| pickle_dict          | 31.2 us                                                | 30.3 us: 1.03x faster                                                        |
| unpickle_list        | 4.99 us                                                | 5.10 us: 1.02x slower                                                        |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.00 ms: 1.05x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.55 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.10x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                        |
| mako            | 9.83 ms                                                | 9.93 ms: 1.01x slower                                                        |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.0 ms: 2.45x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 506 ms: 1.75x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.47 ms: 1.30x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                                         |
| coroutines              | 26.2 ms                                                | 22.3 ms: 1.17x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.15 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                         |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.10x faster                                                        |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                       |
| json                    | 4.87 ms                                                | 4.54 ms: 1.07x faster                                                        |
| richards                | 46.1 ms                                                | 43.2 ms: 1.07x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 289 us: 1.07x faster                                                         |
| html5lib                | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 92.4 ms: 1.06x faster                                                        |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                                        |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 667 ms: 1.06x faster                                                         |
| regex_effbot            | 3.46 ms                                                | 3.27 ms: 1.06x faster                                                        |
| nqueens                 | 83.8 ms                                                | 79.4 ms: 1.05x faster                                                        |
| pyflate                 | 419 ms                                                 | 397 ms: 1.05x faster                                                         |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                         |
| logging_silent          | 98.0 ns                                                | 93.2 ns: 1.05x faster                                                        |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                                         |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                       |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                         |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                         |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                                        |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                         |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                         |
| bench_thread_pool       | 817 us                                                 | 786 us: 1.04x faster                                                         |
| scimark_monte_carlo     | 68.0 ms                                                | 65.4 ms: 1.04x faster                                                        |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                         |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                         |
| pickle_list             | 4.14 us                                                | 4.00 us: 1.03x faster                                                        |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                        |
| chaos                   | 68.7 ms                                                | 66.6 ms: 1.03x faster                                                        |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                         |
| pickle_dict             | 31.2 us                                                | 30.3 us: 1.03x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                        |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 43.5 ns: 1.02x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                        |
| coverage                | 99.3 ms                                                | 97.1 ms: 1.02x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                        |
| tornado_http            | 96.5 ms                                                | 94.9 ms: 1.02x faster                                                        |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                         |
| crypto_pyaes            | 75.7 ms                                                | 74.5 ms: 1.02x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                         |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                         |
| deepcopy_reduce         | 3.02 us                                                | 2.99 us: 1.01x faster                                                        |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                       |
| regex_v8                | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                        |
| mako                    | 9.83 ms                                                | 9.93 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 745 ms: 1.01x slower                                                         |
| thrift                  | 760 us                                                 | 769 us: 1.01x slower                                                         |
| chameleon               | 6.38 ms                                                | 6.48 ms: 1.02x slower                                                        |
| docutils                | 2.60 sec                                               | 2.65 sec: 1.02x slower                                                       |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                        |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.68 ms: 1.02x slower                                                        |
| unpickle_list           | 4.99 us                                                | 5.10 us: 1.02x slower                                                        |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.03x slower                                                        |
| nbody                   | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                        |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                                         |
| async_tree_memoization  | 624 ms                                                 | 654 ms: 1.05x slower                                                         |
| python_startup          | 8.58 ms                                                | 9.00 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.07x slower                                                        |
| gc_traversal            | 3.82 ms                                                | 4.07 ms: 1.07x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.55 ms: 1.08x slower                                                        |
| async_generators        | 356 ms                                                 | 422 ms: 1.19x slower                                                         |
| dask                    | 365 ms                                                 | 499 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (8): djangocms, unpickle, sqlalchemy_imperative, xml_etree_iterparse, sympy_sum, bench_mp_pool, telco, pathlib
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
