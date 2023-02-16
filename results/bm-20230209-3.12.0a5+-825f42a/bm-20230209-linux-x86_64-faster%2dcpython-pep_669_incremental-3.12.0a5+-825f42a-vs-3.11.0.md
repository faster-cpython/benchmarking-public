
# Results vs. 3.11.0

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 825f42a
- commit date: 2023-02-09
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.06x faster                                                            |
| chameleon      | 6.38 ms                                                | 6.23 ms: 1.02x faster                                                           |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                          |
| html5lib       | 64.8 ms                                                | 58.7 ms: 1.10x faster                                                           |
| tornado_http   | 96.5 ms                                                | 92.8 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.4 ms: 1.08x faster                                                           |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                            |
| nbody          | 90.0 ms                                                | 90.7 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 124 ms: 1.10x faster                                                            |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                           |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                                            |
| regex_effbot   | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                                           |
| unpickle_pure_python | 227 us                                                 | 194 us: 1.17x faster                                                            |
| pickle_pure_python   | 308 us                                                 | 279 us: 1.11x faster                                                            |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                                           |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                            |
| pickle_dict          | 31.2 us                                                | 29.4 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                            |
| pickle_list          | 4.14 us                                                | 4.04 us: 1.03x faster                                                           |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                                           |
| unpickle             | 13.3 us                                                | 13.5 us: 1.02x slower                                                           |
| xml_etree_process    | 53.7 ms                                                | 55.1 ms: 1.03x slower                                                           |
| unpickle_list        | 4.99 us                                                | 5.15 us: 1.03x slower                                                           |
| xml_etree_generate   | 75.9 ms                                                | 79.6 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.94 ms: 1.04x slower                                                           |
| python_startup_no_site | 6.04 ms                                                | 6.50 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 45.5 ms: 1.13x faster                                                           |
| genshi_text    | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                            |
| generators              | 73.5 ms                                                | 54.8 ms: 1.34x faster                                                           |
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                                           |
| mypy2                   | 420 ms                                                 | 322 ms: 1.31x faster                                                            |
| deltablue               | 3.66 ms                                                | 3.11 ms: 1.17x faster                                                           |
| unpickle_pure_python    | 227 us                                                 | 194 us: 1.17x faster                                                            |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.92 ms: 1.17x faster                                                           |
| genshi_xml              | 51.4 ms                                                | 45.5 ms: 1.13x faster                                                           |
| scimark_sor             | 115 ms                                                 | 102 ms: 1.13x faster                                                            |
| richards                | 46.1 ms                                                | 41.2 ms: 1.12x faster                                                           |
| nqueens                 | 83.8 ms                                                | 75.5 ms: 1.11x faster                                                           |
| pickle_pure_python      | 308 us                                                 | 279 us: 1.11x faster                                                            |
| html5lib                | 64.8 ms                                                | 58.7 ms: 1.10x faster                                                           |
| regex_compile           | 136 ms                                                 | 124 ms: 1.10x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.10x faster                                                          |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                                           |
| chaos                   | 68.7 ms                                                | 62.6 ms: 1.10x faster                                                           |
| sympy_str               | 291 ms                                                 | 265 ms: 1.10x faster                                                            |
| hexiom                  | 6.34 ms                                                | 5.79 ms: 1.10x faster                                                           |
| go                      | 140 ms                                                 | 129 ms: 1.09x faster                                                            |
| scimark_fft             | 325 ms                                                 | 299 ms: 1.09x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                            |
| float                   | 76.8 ms                                                | 71.4 ms: 1.08x faster                                                           |
| deepcopy_memo           | 35.8 us                                                | 33.3 us: 1.08x faster                                                           |
| sympy_integrate         | 21.0 ms                                                | 19.5 ms: 1.07x faster                                                           |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                            |
| aiohttp                 | 1.05 ms                                                | 983 us: 1.07x faster                                                            |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                                           |
| logging_simple          | 6.02 us                                                | 5.65 us: 1.07x faster                                                           |
| sympy_expand            | 475 ms                                                 | 446 ms: 1.07x faster                                                            |
| scimark_monte_carlo     | 68.0 ms                                                | 63.8 ms: 1.07x faster                                                           |
| unpack_sequence         | 44.5 ns                                                | 41.8 ns: 1.07x faster                                                           |
| fannkuch                | 384 ms                                                 | 361 ms: 1.06x faster                                                            |
| deepcopy                | 341 us                                                 | 321 us: 1.06x faster                                                            |
| pickle_dict             | 31.2 us                                                | 29.4 us: 1.06x faster                                                           |
| gunicorn                | 1.12 ms                                                | 1.05 ms: 1.06x faster                                                           |
| bench_thread_pool       | 817 us                                                 | 771 us: 1.06x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                          |
| sqlglot_optimize        | 52.7 ms                                                | 49.8 ms: 1.06x faster                                                           |
| raytrace                | 291 ms                                                 | 276 ms: 1.06x faster                                                            |
| 2to3                    | 259 ms                                                 | 246 ms: 1.06x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| pprint_safe_repr        | 706 ms                                                 | 668 ms: 1.06x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.05x faster                                                            |
| logging_silent          | 98.0 ns                                                | 93.1 ns: 1.05x faster                                                           |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                           |
| scimark_lu              | 108 ms                                                 | 103 ms: 1.05x faster                                                            |
| spectral_norm           | 98.1 ms                                                | 93.3 ms: 1.05x faster                                                           |
| crypto_pyaes            | 75.7 ms                                                | 72.1 ms: 1.05x faster                                                           |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.3 ms: 1.05x faster                                                           |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                          |
| tornado_http            | 96.5 ms                                                | 92.8 ms: 1.04x faster                                                           |
| dulwich_log             | 64.0 ms                                                | 61.5 ms: 1.04x faster                                                           |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                            |
| logging_format          | 6.48 us                                                | 6.26 us: 1.04x faster                                                           |
| sqlalchemy_declarative  | 138 ms                                                 | 134 ms: 1.03x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                           |
| pickle_list             | 4.14 us                                                | 4.04 us: 1.03x faster                                                           |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                            |
| chameleon               | 6.38 ms                                                | 6.23 ms: 1.02x faster                                                           |
| pyflate                 | 419 ms                                                 | 410 ms: 1.02x faster                                                            |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                           |
| coverage                | 99.3 ms                                                | 97.7 ms: 1.02x faster                                                           |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                           |
| telco                   | 6.43 ms                                                | 6.35 ms: 1.01x faster                                                           |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                            |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                                            |
| gc_traversal            | 3.82 ms                                                | 3.80 ms: 1.00x faster                                                           |
| nbody                   | 90.0 ms                                                | 90.7 ms: 1.01x slower                                                           |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                                           |
| mdp                     | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                          |
| unpickle                | 13.3 us                                                | 13.5 us: 1.02x slower                                                           |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                           |
| xml_etree_process       | 53.7 ms                                                | 55.1 ms: 1.03x slower                                                           |
| async_tree_memoization  | 624 ms                                                 | 643 ms: 1.03x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                           |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                          |
| regex_effbot            | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                           |
| unpickle_list           | 4.99 us                                                | 5.15 us: 1.03x slower                                                           |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                           |
| async_tree_cpu_io_mixed | 736 ms                                                 | 767 ms: 1.04x slower                                                            |
| python_startup          | 8.58 ms                                                | 8.94 ms: 1.04x slower                                                           |
| xml_etree_generate      | 75.9 ms                                                | 79.6 ms: 1.05x slower                                                           |
| python_startup_no_site  | 6.04 ms                                                | 6.50 ms: 1.08x slower                                                           |
| async_generators        | 356 ms                                                 | 420 ms: 1.18x slower                                                            |
| coroutines              | 26.2 ms                                                | 54.8 ms: 2.10x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (6): djangocms, mako, django_template, bench_mp_pool, thrift, async_tree_none
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
