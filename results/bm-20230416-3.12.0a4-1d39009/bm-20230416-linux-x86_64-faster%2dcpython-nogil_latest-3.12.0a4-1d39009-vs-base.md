
# Results vs. base

- fork: faster-cpython
- ref: nogil_latest
- machine: linux-x86_64
- commit hash: 1d39009
- commit date: 2023-04-16
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 290 ms: 1.15x slower                                                    |
| chameleon      | 6.46 ms                                                               | 7.81 ms: 1.21x slower                                                   |
| docutils       | 2.48 sec                                                              | 3.15 sec: 1.27x slower                                                  |
| html5lib       | 59.8 ms                                                               | 69.2 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 72.2 ms                                                               | 65.9 ms: 1.10x faster                                                   |
| pidigits       | 192 ms                                                                | 186 ms: 1.04x faster                                                    |
| nbody          | 93.1 ms                                                               | 107 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 209 ms                                                                | 205 ms: 1.02x faster                                                    |
| regex_effbot   | 3.49 ms                                                               | 3.46 ms: 1.01x faster                                                   |
| regex_compile  | 132 ms                                                                | 152 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 149 ms                                                                | 137 ms: 1.09x faster                                                    |
| pickle               | 10.0 us                                                               | 10.3 us: 1.03x slower                                                   |
| unpickle_list        | 4.96 us                                                               | 5.20 us: 1.05x slower                                                   |
| xml_etree_iterparse  | 106 ms                                                                | 114 ms: 1.07x slower                                                    |
| pickle_list          | 4.02 us                                                               | 4.33 us: 1.08x slower                                                   |
| xml_etree_generate   | 77.5 ms                                                               | 83.7 ms: 1.08x slower                                                   |
| json_dumps           | 9.54 ms                                                               | 10.4 ms: 1.09x slower                                                   |
| pickle_pure_python   | 285 us                                                                | 321 us: 1.12x slower                                                    |
| xml_etree_process    | 53.9 ms                                                               | 61.3 ms: 1.14x slower                                                   |
| unpickle_pure_python | 200 us                                                                | 229 us: 1.15x slower                                                    |
| json_loads           | 24.3 us                                                               | 28.0 us: 1.15x slower                                                   |
| unpickle             | 13.0 us                                                               | 15.5 us: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.54 ms                                                               | 9.18 ms: 1.07x slower                                                   |
| python_startup_no_site | 6.09 ms                                                               | 6.59 ms: 1.08x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 46.5 ms                                                               | 52.0 ms: 1.12x slower                                                   |
| django_template | 32.6 ms                                                               | 37.4 ms: 1.15x slower                                                   |
| genshi_text     | 20.8 ms                                                               | 24.4 ms: 1.17x slower                                                   |
| mako            | 9.74 ms                                                               | 13.2 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark               | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                                              | 616 ms: 2.10x faster                                                    |
| async_tree_none         | 521 ms                                                                | 311 ms: 1.67x faster                                                    |
| async_tree_memoization  | 616 ms                                                                | 381 ms: 1.62x faster                                                    |
| async_tree_cpu_io_mixed | 747 ms                                                                | 534 ms: 1.40x faster                                                    |
| float                   | 72.2 ms                                                               | 65.9 ms: 1.10x faster                                                   |
| xml_etree_parse         | 149 ms                                                                | 137 ms: 1.09x faster                                                    |
| pidigits                | 192 ms                                                                | 186 ms: 1.04x faster                                                    |
| regex_dna               | 209 ms                                                                | 205 ms: 1.02x faster                                                    |
| regex_effbot            | 3.49 ms                                                               | 3.46 ms: 1.01x faster                                                   |
| bench_mp_pool           | 24.0 ms                                                               | 23.8 ms: 1.01x faster                                                   |
| generators              | 79.1 ms                                                               | 78.8 ms: 1.00x faster                                                   |
| pathlib                 | 18.0 ms                                                               | 18.2 ms: 1.01x slower                                                   |
| sqlite_synth            | 2.57 us                                                               | 2.62 us: 1.02x slower                                                   |
| pickle                  | 10.0 us                                                               | 10.3 us: 1.03x slower                                                   |
| gc_traversal            | 3.57 ms                                                               | 3.67 ms: 1.03x slower                                                   |
| asyncio_tcp             | 504 ms                                                                | 525 ms: 1.04x slower                                                    |
| unpickle_list           | 4.96 us                                                               | 5.20 us: 1.05x slower                                                   |
| mdp                     | 2.66 sec                                                              | 2.79 sec: 1.05x slower                                                  |
| coroutines              | 25.4 ms                                                               | 26.8 ms: 1.05x slower                                                   |
| async_generators        | 354 ms                                                                | 377 ms: 1.07x slower                                                    |
| pycparser               | 1.08 sec                                                              | 1.15 sec: 1.07x slower                                                  |
| xml_etree_iterparse     | 106 ms                                                                | 114 ms: 1.07x slower                                                    |
| json                    | 4.74 ms                                                               | 5.06 ms: 1.07x slower                                                   |
| python_startup          | 8.54 ms                                                               | 9.18 ms: 1.07x slower                                                   |
| pickle_list             | 4.02 us                                                               | 4.33 us: 1.08x slower                                                   |
| crypto_pyaes            | 75.7 ms                                                               | 81.8 ms: 1.08x slower                                                   |
| xml_etree_generate      | 77.5 ms                                                               | 83.7 ms: 1.08x slower                                                   |
| python_startup_no_site  | 6.09 ms                                                               | 6.59 ms: 1.08x slower                                                   |
| go                      | 135 ms                                                                | 146 ms: 1.08x slower                                                    |
| json_dumps              | 9.54 ms                                                               | 10.4 ms: 1.09x slower                                                   |
| create_gc_cycles        | 1.45 ms                                                               | 1.59 ms: 1.10x slower                                                   |
| dulwich_log             | 62.1 ms                                                               | 68.1 ms: 1.10x slower                                                   |
| nqueens                 | 78.0 ms                                                               | 85.8 ms: 1.10x slower                                                   |
| chaos                   | 67.7 ms                                                               | 74.6 ms: 1.10x slower                                                   |
| sqlglot_normalize       | 104 ms                                                                | 115 ms: 1.10x slower                                                    |
| coverage                | 99.0 ms                                                               | 109 ms: 1.10x slower                                                    |
| telco                   | 6.26 ms                                                               | 6.92 ms: 1.11x slower                                                   |
| deepcopy                | 339 us                                                                | 375 us: 1.11x slower                                                    |
| logging_silent          | 93.5 ns                                                               | 104 ns: 1.11x slower                                                    |
| comprehensions          | 23.7 us                                                               | 26.3 us: 1.11x slower                                                   |
| genshi_xml              | 46.5 ms                                                               | 52.0 ms: 1.12x slower                                                   |
| sympy_integrate         | 20.3 ms                                                               | 22.8 ms: 1.12x slower                                                   |
| pickle_pure_python      | 285 us                                                                | 321 us: 1.12x slower                                                    |
| pprint_safe_repr        | 680 ms                                                                | 765 ms: 1.12x slower                                                    |
| sqlglot_optimize        | 50.7 ms                                                               | 57.1 ms: 1.13x slower                                                   |
| thrift                  | 752 us                                                                | 851 us: 1.13x slower                                                    |
| scimark_sor             | 108 ms                                                                | 123 ms: 1.13x slower                                                    |
| xml_etree_process       | 53.9 ms                                                               | 61.3 ms: 1.14x slower                                                   |
| richards                | 42.3 ms                                                               | 48.4 ms: 1.14x slower                                                   |
| pprint_pformat          | 1.38 sec                                                              | 1.58 sec: 1.14x slower                                                  |
| deepcopy_reduce         | 2.99 us                                                               | 3.42 us: 1.14x slower                                                   |
| unpickle_pure_python    | 200 us                                                                | 229 us: 1.15x slower                                                    |
| django_template         | 32.6 ms                                                               | 37.4 ms: 1.15x slower                                                   |
| 2to3                    | 253 ms                                                                | 290 ms: 1.15x slower                                                    |
| nbody                   | 93.1 ms                                                               | 107 ms: 1.15x slower                                                    |
| json_loads              | 24.3 us                                                               | 28.0 us: 1.15x slower                                                   |
| regex_compile           | 132 ms                                                                | 152 ms: 1.15x slower                                                    |
| hexiom                  | 5.98 ms                                                               | 6.89 ms: 1.15x slower                                                   |
| html5lib                | 59.8 ms                                                               | 69.2 ms: 1.16x slower                                                   |
| deepcopy_memo           | 34.7 us                                                               | 40.1 us: 1.16x slower                                                   |
| scimark_monte_carlo     | 65.7 ms                                                               | 76.4 ms: 1.16x slower                                                   |
| sympy_str               | 282 ms                                                                | 329 ms: 1.17x slower                                                    |
| genshi_text             | 20.8 ms                                                               | 24.4 ms: 1.17x slower                                                   |
| spectral_norm           | 95.0 ms                                                               | 112 ms: 1.18x slower                                                    |
| sympy_sum               | 163 ms                                                                | 192 ms: 1.18x slower                                                    |
| sympy_expand            | 455 ms                                                                | 537 ms: 1.18x slower                                                    |
| pyflate                 | 397 ms                                                                | 470 ms: 1.18x slower                                                    |
| scimark_lu              | 107 ms                                                                | 128 ms: 1.19x slower                                                    |
| meteor_contest          | 104 ms                                                                | 124 ms: 1.19x slower                                                    |
| unpickle                | 13.0 us                                                               | 15.5 us: 1.19x slower                                                   |
| scimark_sparse_mat_mult | 4.13 ms                                                               | 4.94 ms: 1.20x slower                                                   |
| fannkuch                | 362 ms                                                                | 436 ms: 1.20x slower                                                    |
| deltablue               | 3.25 ms                                                               | 3.91 ms: 1.20x slower                                                   |
| logging_format          | 6.35 us                                                               | 7.66 us: 1.21x slower                                                   |
| chameleon               | 6.46 ms                                                               | 7.81 ms: 1.21x slower                                                   |
| logging_simple          | 5.77 us                                                               | 7.00 us: 1.21x slower                                                   |
| raytrace                | 284 ms                                                                | 346 ms: 1.22x slower                                                    |
| scimark_fft             | 314 ms                                                                | 383 ms: 1.22x slower                                                    |
| djangocms               | 30.9 us                                                               | 37.9 us: 1.22x slower                                                   |
| sqlglot_transpile       | 1.69 ms                                                               | 2.10 ms: 1.24x slower                                                   |
| docutils                | 2.48 sec                                                              | 3.15 sec: 1.27x slower                                                  |
| sqlglot_parse           | 1.41 ms                                                               | 1.79 ms: 1.27x slower                                                   |
| mako                    | 9.74 ms                                                               | 13.2 ms: 1.36x slower                                                   |
| mypy2                   | 332 ms                                                                | 457 ms: 1.38x slower                                                    |
| unpack_sequence         | 41.4 ns                                                               | 58.1 ns: 1.40x slower                                                   |
| bench_thread_pool       | 782 us                                                                | 1.64 ms: 2.10x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, pickle_dict
Ignored benchmarks (1) of results/bm-20230110-3.12.0a4-3d5d3f7/bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x
