
# Results vs. 3.11.0

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.24x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 335 ms: 1.30x slower                                     |
| chameleon      | 6.52 ms                                                             | 9.13 ms: 1.40x slower                                    |
| docutils       | 2.59 sec                                                            | 3.22 sec: 1.24x slower                                   |
| html5lib       | 64.0 ms                                                             | 87.5 ms: 1.37x slower                                    |
| tornado_http   | 96.7 ms                                                             | 130 ms: 1.35x slower                                     |
| Geometric mean | (ref)                                                               | 1.33x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                     |
| nbody          | 96.7 ms                                                             | 137 ms: 1.42x slower                                     |
| float          | 76.0 ms                                                             | 109 ms: 1.43x slower                                     |
| Geometric mean | (ref)                                                               | 1.25x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.62 ms: 1.09x slower                                    |
| regex_v8       | 22.0 ms                                                             | 24.1 ms: 1.10x slower                                    |
| regex_dna      | 196 ms                                                              | 216 ms: 1.10x slower                                     |
| regex_compile  | 137 ms                                                              | 177 ms: 1.29x slower                                     |
| Geometric mean | (ref)                                                               | 1.14x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 30.5 us: 1.01x faster                                    |
| xml_etree_iterparse  | 108 ms                                                              | 110 ms: 1.03x slower                                     |
| pickle_list          | 4.03 us                                                             | 4.17 us: 1.04x slower                                    |
| pickle               | 9.79 us                                                             | 10.2 us: 1.04x slower                                    |
| json_dumps           | 12.5 ms                                                             | 13.6 ms: 1.09x slower                                    |
| json_loads           | 26.2 us                                                             | 29.2 us: 1.12x slower                                    |
| unpickle             | 13.2 us                                                             | 14.8 us: 1.12x slower                                    |
| xml_etree_generate   | 76.5 ms                                                             | 93.0 ms: 1.22x slower                                    |
| unpickle_pure_python | 228 us                                                              | 297 us: 1.30x slower                                     |
| xml_etree_process    | 54.1 ms                                                             | 74.4 ms: 1.38x slower                                    |
| pickle_pure_python   | 307 us                                                              | 449 us: 1.46x slower                                     |
| Geometric mean       | (ref)                                                               | 1.13x slower                                             |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 5.98 ms                                                             | 5.79 ms: 1.03x faster                                    |
| python_startup         | 8.49 ms                                                             | 9.33 ms: 1.10x slower                                    |
| Geometric mean         | (ref)                                                               | 1.03x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 62.6 ms: 1.21x slower                                    |
| genshi_text     | 21.8 ms                                                             | 30.1 ms: 1.38x slower                                    |
| django_template | 32.9 ms                                                             | 46.6 ms: 1.42x slower                                    |
| mako            | 9.82 ms                                                             | 14.6 ms: 1.49x slower                                    |
| Geometric mean  | (ref)                                                               | 1.37x slower                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| coverage                | 101 ms                                                              | 71.5 ms: 1.41x faster                                    |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                     |
| python_startup_no_site  | 5.98 ms                                                             | 5.79 ms: 1.03x faster                                    |
| gc_traversal            | 3.63 ms                                                             | 3.54 ms: 1.02x faster                                    |
| pickle_dict             | 30.9 us                                                             | 30.5 us: 1.01x faster                                    |
| telco                   | 6.59 ms                                                             | 6.71 ms: 1.02x slower                                    |
| xml_etree_iterparse     | 108 ms                                                              | 110 ms: 1.03x slower                                     |
| asyncio_tcp             | 888 ms                                                              | 915 ms: 1.03x slower                                     |
| pickle_list             | 4.03 us                                                             | 4.17 us: 1.04x slower                                    |
| generators              | 73.4 ms                                                             | 76.1 ms: 1.04x slower                                    |
| pickle                  | 9.79 us                                                             | 10.2 us: 1.04x slower                                    |
| meteor_contest          | 106 ms                                                              | 113 ms: 1.06x slower                                     |
| mdp                     | 2.64 sec                                                            | 2.82 sec: 1.07x slower                                   |
| pathlib                 | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                    |
| json_dumps              | 12.5 ms                                                             | 13.6 ms: 1.09x slower                                    |
| regex_effbot            | 3.32 ms                                                             | 3.62 ms: 1.09x slower                                    |
| python_startup          | 8.49 ms                                                             | 9.33 ms: 1.10x slower                                    |
| regex_v8                | 22.0 ms                                                             | 24.1 ms: 1.10x slower                                    |
| pylint                  | 476 ms                                                              | 524 ms: 1.10x slower                                     |
| regex_dna               | 196 ms                                                              | 216 ms: 1.10x slower                                     |
| create_gc_cycles        | 1.48 ms                                                             | 1.63 ms: 1.10x slower                                    |
| json                    | 4.86 ms                                                             | 5.40 ms: 1.11x slower                                    |
| json_loads              | 26.2 us                                                             | 29.2 us: 1.12x slower                                    |
| unpickle                | 13.2 us                                                             | 14.8 us: 1.12x slower                                    |
| bench_thread_pool       | 820 us                                                              | 919 us: 1.12x slower                                     |
| sympy_sum               | 167 ms                                                              | 189 ms: 1.13x slower                                     |
| sympy_str               | 291 ms                                                              | 329 ms: 1.13x slower                                     |
| djangocms               | 32.3 us                                                             | 36.7 us: 1.14x slower                                    |
| sympy_expand            | 477 ms                                                              | 546 ms: 1.15x slower                                     |
| sympy_integrate         | 21.0 ms                                                             | 24.4 ms: 1.16x slower                                    |
| sqlalchemy_imperative   | 18.0 ms                                                             | 20.9 ms: 1.16x slower                                    |
| coroutines              | 26.3 ms                                                             | 30.6 ms: 1.17x slower                                    |
| async_generators        | 361 ms                                                              | 426 ms: 1.18x slower                                     |
| dask                    | 368 ms                                                              | 434 ms: 1.18x slower                                     |
| sqlite_synth            | 2.51 us                                                             | 2.97 us: 1.18x slower                                    |
| dulwich_log             | 63.6 ms                                                             | 75.4 ms: 1.18x slower                                    |
| nqueens                 | 84.0 ms                                                             | 100 ms: 1.19x slower                                     |
| flaskblogging           | 7.09 ms                                                             | 8.47 ms: 1.20x slower                                    |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 5.39 ms: 1.21x slower                                    |
| sqlalchemy_declarative  | 138 ms                                                              | 167 ms: 1.21x slower                                     |
| genshi_xml              | 51.8 ms                                                             | 62.6 ms: 1.21x slower                                    |
| xml_etree_generate      | 76.5 ms                                                             | 93.0 ms: 1.22x slower                                    |
| fannkuch                | 384 ms                                                              | 467 ms: 1.22x slower                                     |
| sqlglot_optimize        | 53.4 ms                                                             | 65.4 ms: 1.23x slower                                    |
| aiohttp                 | 1.05 ms                                                             | 1.29 ms: 1.23x slower                                    |
| gunicorn                | 1.13 ms                                                             | 1.39 ms: 1.23x slower                                    |
| docutils                | 2.59 sec                                                            | 3.22 sec: 1.24x slower                                   |
| scimark_fft             | 328 ms                                                              | 408 ms: 1.25x slower                                     |
| sqlglot_normalize       | 108 ms                                                              | 136 ms: 1.25x slower                                     |
| deepcopy                | 339 us                                                              | 428 us: 1.26x slower                                     |
| deepcopy_reduce         | 2.96 us                                                             | 3.81 us: 1.29x slower                                    |
| regex_compile           | 137 ms                                                              | 177 ms: 1.29x slower                                     |
| unpack_sequence         | 49.5 ns                                                             | 64.0 ns: 1.29x slower                                    |
| unpickle_pure_python    | 228 us                                                              | 297 us: 1.30x slower                                     |
| 2to3                    | 257 ms                                                              | 335 ms: 1.30x slower                                     |
| pycparser               | 1.14 sec                                                            | 1.54 sec: 1.34x slower                                   |
| tornado_http            | 96.7 ms                                                             | 130 ms: 1.35x slower                                     |
| thrift                  | 766 us                                                              | 1.04 ms: 1.35x slower                                    |
| async_tree_cpu_io_mixed | 736 ms                                                              | 997 ms: 1.36x slower                                     |
| html5lib                | 64.0 ms                                                             | 87.5 ms: 1.37x slower                                    |
| deepcopy_memo           | 36.4 us                                                             | 49.9 us: 1.37x slower                                    |
| async_tree_none         | 525 ms                                                              | 721 ms: 1.37x slower                                     |
| xml_etree_process       | 54.1 ms                                                             | 74.4 ms: 1.38x slower                                    |
| genshi_text             | 21.8 ms                                                             | 30.1 ms: 1.38x slower                                    |
| async_tree_memoization  | 621 ms                                                              | 856 ms: 1.38x slower                                     |
| logging_simple          | 6.09 us                                                             | 8.41 us: 1.38x slower                                    |
| logging_format          | 6.64 us                                                             | 9.20 us: 1.39x slower                                    |
| pprint_safe_repr        | 701 ms                                                              | 975 ms: 1.39x slower                                     |
| pprint_pformat          | 1.45 sec                                                            | 2.02 sec: 1.39x slower                                   |
| async_tree_io           | 1.28 sec                                                            | 1.78 sec: 1.39x slower                                   |
| chameleon               | 6.52 ms                                                             | 9.13 ms: 1.40x slower                                    |
| django_template         | 32.9 ms                                                             | 46.6 ms: 1.42x slower                                    |
| nbody                   | 96.7 ms                                                             | 137 ms: 1.42x slower                                     |
| float                   | 76.0 ms                                                             | 109 ms: 1.43x slower                                     |
| spectral_norm           | 99.5 ms                                                             | 143 ms: 1.44x slower                                     |
| hexiom                  | 6.48 ms                                                             | 9.42 ms: 1.45x slower                                    |
| sqlglot_transpile       | 1.65 ms                                                             | 2.41 ms: 1.46x slower                                    |
| pickle_pure_python      | 307 us                                                              | 449 us: 1.46x slower                                     |
| scimark_lu              | 108 ms                                                              | 160 ms: 1.48x slower                                     |
| sqlglot_parse           | 1.36 ms                                                             | 2.03 ms: 1.49x slower                                    |
| mako                    | 9.82 ms                                                             | 14.6 ms: 1.49x slower                                    |
| scimark_monte_carlo     | 67.8 ms                                                             | 105 ms: 1.55x slower                                     |
| crypto_pyaes            | 73.8 ms                                                             | 115 ms: 1.56x slower                                     |
| chaos                   | 68.0 ms                                                             | 106 ms: 1.56x slower                                     |
| raytrace                | 292 ms                                                              | 463 ms: 1.58x slower                                     |
| richards                | 45.7 ms                                                             | 72.6 ms: 1.59x slower                                    |
| pyflate                 | 414 ms                                                              | 659 ms: 1.59x slower                                     |
| go                      | 138 ms                                                              | 226 ms: 1.64x slower                                     |
| scimark_sor             | 115 ms                                                              | 193 ms: 1.68x slower                                     |
| logging_silent          | 98.7 ns                                                             | 174 ns: 1.77x slower                                     |
| deltablue               | 3.66 ms                                                             | 7.41 ms: 2.03x slower                                    |
| Geometric mean          | (ref)                                                               | 1.24x slower                                             |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_list, bench_mp_pool, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: comprehensions
