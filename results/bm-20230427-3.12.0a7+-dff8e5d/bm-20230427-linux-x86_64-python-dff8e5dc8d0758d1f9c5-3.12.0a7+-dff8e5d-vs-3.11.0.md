
# Results vs. 3.11.0

- fork: python
- ref: dff8e5dc8d0758d1f9c5
- machine: linux-x86_64
- commit hash: dff8e5d
- commit date: 2023-04-27
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 267 ms: 1.04x slower                                                   |
| chameleon      | 6.52 ms                                                             | 6.90 ms: 1.06x slower                                                  |
| docutils       | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 105 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.9 ms: 1.09x faster                                                  |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| float          | 76.0 ms                                                             | 81.6 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.1 ms: 1.00x slower                                                  |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                                   |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| regex_effbot   | 3.32 ms                                                             | 3.79 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.1 ms: 1.24x faster                                                  |
| xml_etree_parse      | 162 ms                                                              | 151 ms: 1.07x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 216 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                                   |
| unpickle_list        | 4.96 us                                                             | 4.86 us: 1.02x faster                                                  |
| json_loads           | 26.2 us                                                             | 25.9 us: 1.01x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 316 us: 1.03x slower                                                   |
| pickle_dict          | 30.9 us                                                             | 32.3 us: 1.05x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 58.6 ms: 1.08x slower                                                  |
| pickle               | 9.79 us                                                             | 10.7 us: 1.10x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.7 ms: 1.11x slower                                                  |
| unpickle             | 13.2 us                                                             | 14.8 us: 1.12x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.64 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.07 ms: 1.07x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.66 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 50.2 ms: 1.03x faster                                                  |
| genshi_text     | 21.8 ms                                                             | 22.4 ms: 1.03x slower                                                  |
| django_template | 32.9 ms                                                             | 35.1 ms: 1.07x slower                                                  |
| mako            | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.7 ms: 2.39x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 506 ms: 1.75x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 10.1 ms: 1.24x faster                                                  |
| mypy2                   | 422 ms                                                              | 349 ms: 1.21x faster                                                   |
| coroutines              | 26.3 ms                                                             | 22.3 ms: 1.18x faster                                                  |
| nbody                   | 96.7 ms                                                             | 88.9 ms: 1.09x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 151 ms: 1.07x faster                                                   |
| hexiom                  | 6.48 ms                                                             | 6.11 ms: 1.06x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 216 us: 1.06x faster                                                   |
| unpack_sequence         | 49.5 ns                                                             | 47.3 ns: 1.05x faster                                                  |
| richards                | 45.7 ms                                                             | 43.7 ms: 1.04x faster                                                  |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                                   |
| nqueens                 | 84.0 ms                                                             | 81.3 ms: 1.03x faster                                                  |
| deltablue               | 3.66 ms                                                             | 3.54 ms: 1.03x faster                                                  |
| genshi_xml              | 51.8 ms                                                             | 50.2 ms: 1.03x faster                                                  |
| fannkuch                | 384 ms                                                              | 373 ms: 1.03x faster                                                   |
| pathlib                 | 18.2 ms                                                             | 17.8 ms: 1.02x faster                                                  |
| unpickle_list           | 4.96 us                                                             | 4.86 us: 1.02x faster                                                  |
| mdp                     | 2.64 sec                                                            | 2.59 sec: 1.02x faster                                                 |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                  |
| pycparser               | 1.14 sec                                                            | 1.13 sec: 1.01x faster                                                 |
| json_loads              | 26.2 us                                                             | 25.9 us: 1.01x faster                                                  |
| go                      | 138 ms                                                              | 138 ms: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                             | 22.1 ms: 1.00x slower                                                  |
| bench_thread_pool       | 820 us                                                              | 830 us: 1.01x slower                                                   |
| scimark_lu              | 108 ms                                                              | 110 ms: 1.01x slower                                                   |
| chaos                   | 68.0 ms                                                             | 69.0 ms: 1.02x slower                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.50 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 749 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 54.6 ms: 1.02x slower                                                  |
| json                    | 4.86 ms                                                             | 4.98 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.02x slower                                                   |
| genshi_text             | 21.8 ms                                                             | 22.4 ms: 1.03x slower                                                  |
| logging_simple          | 6.09 us                                                             | 6.26 us: 1.03x slower                                                  |
| pprint_pformat          | 1.45 sec                                                            | 1.49 sec: 1.03x slower                                                 |
| pickle_pure_python      | 307 us                                                              | 316 us: 1.03x slower                                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.62 ms: 1.03x slower                                                  |
| sympy_integrate         | 21.0 ms                                                             | 21.8 ms: 1.04x slower                                                  |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                                   |
| raytrace                | 292 ms                                                              | 304 ms: 1.04x slower                                                   |
| 2to3                    | 257 ms                                                              | 267 ms: 1.04x slower                                                   |
| comprehensions          | 22.2 us                                                             | 23.2 us: 1.04x slower                                                  |
| pprint_safe_repr        | 701 ms                                                              | 731 ms: 1.04x slower                                                   |
| djangocms               | 32.3 us                                                             | 33.7 us: 1.04x slower                                                  |
| logging_format          | 6.64 us                                                             | 6.93 us: 1.04x slower                                                  |
| pickle_dict             | 30.9 us                                                             | 32.3 us: 1.05x slower                                                  |
| docutils                | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                 |
| telco                   | 6.59 ms                                                             | 6.89 ms: 1.05x slower                                                  |
| async_tree_memoization  | 621 ms                                                              | 650 ms: 1.05x slower                                                   |
| thrift                  | 766 us                                                              | 801 us: 1.05x slower                                                   |
| logging_silent          | 98.7 ns                                                             | 103 ns: 1.05x slower                                                   |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.05x slower                                                   |
| sympy_expand            | 477 ms                                                              | 503 ms: 1.06x slower                                                   |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| chameleon               | 6.52 ms                                                             | 6.90 ms: 1.06x slower                                                  |
| sympy_str               | 291 ms                                                              | 309 ms: 1.06x slower                                                   |
| crypto_pyaes            | 73.8 ms                                                             | 78.5 ms: 1.06x slower                                                  |
| django_template         | 32.9 ms                                                             | 35.1 ms: 1.07x slower                                                  |
| spectral_norm           | 99.5 ms                                                             | 106 ms: 1.07x slower                                                   |
| python_startup          | 8.49 ms                                                             | 9.07 ms: 1.07x slower                                                  |
| dulwich_log             | 63.6 ms                                                             | 68.0 ms: 1.07x slower                                                  |
| deepcopy_memo           | 36.4 us                                                             | 38.9 us: 1.07x slower                                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.8 ms: 1.07x slower                                                  |
| float                   | 76.0 ms                                                             | 81.6 ms: 1.07x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.18 us: 1.08x slower                                                  |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.4 ms: 1.08x slower                                                  |
| sympy_sum               | 167 ms                                                              | 180 ms: 1.08x slower                                                   |
| meteor_contest          | 106 ms                                                              | 114 ms: 1.08x slower                                                   |
| deepcopy                | 339 us                                                              | 366 us: 1.08x slower                                                   |
| xml_etree_process       | 54.1 ms                                                             | 58.6 ms: 1.08x slower                                                  |
| tornado_http            | 96.7 ms                                                             | 105 ms: 1.08x slower                                                   |
| sqlite_synth            | 2.51 us                                                             | 2.73 us: 1.08x slower                                                  |
| pyflate                 | 414 ms                                                              | 450 ms: 1.09x slower                                                   |
| gc_traversal            | 3.63 ms                                                             | 3.95 ms: 1.09x slower                                                  |
| mako                    | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                  |
| scimark_sor             | 115 ms                                                              | 126 ms: 1.09x slower                                                   |
| scimark_fft             | 328 ms                                                              | 359 ms: 1.09x slower                                                   |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.10x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 84.7 ms: 1.11x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.66 ms: 1.11x slower                                                  |
| unpickle                | 13.2 us                                                             | 14.8 us: 1.12x slower                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.79 ms: 1.14x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.64 us: 1.15x slower                                                  |
| async_generators        | 361 ms                                                              | 440 ms: 1.22x slower                                                   |
| dask                    | 368 ms                                                              | 538 ms: 1.46x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (7): pylint, bench_mp_pool, sqlglot_transpile, async_tree_io, coverage, async_tree_none, html5lib
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn
