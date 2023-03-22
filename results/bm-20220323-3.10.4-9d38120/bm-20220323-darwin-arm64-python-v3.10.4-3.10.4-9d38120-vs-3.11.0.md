
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: darwin-arm64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.23x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 201 ms: 1.11x slower                                   |
| chameleon      | 4.61 ms                                                             | 5.79 ms: 1.26x slower                                  |
| docutils       | 1.46 sec                                                            | 1.78 sec: 1.22x slower                                 |
| html5lib       | 34.7 ms                                                             | 44.2 ms: 1.28x slower                                  |
| tornado_http   | 70.6 ms                                                             | 91.5 ms: 1.30x slower                                  |
| Geometric mean | (ref)                                                               | 1.23x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| float          | 51.7 ms                                                             | 72.4 ms: 1.40x slower                                  |
| nbody          | 65.2 ms                                                             | 93.3 ms: 1.43x slower                                  |
| Geometric mean | (ref)                                                               | 1.26x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.46 ms: 1.07x faster                                  |
| regex_v8       | 16.5 ms                                                             | 17.6 ms: 1.07x slower                                  |
| regex_dna      | 151 ms                                                              | 162 ms: 1.07x slower                                   |
| regex_compile  | 76.3 ms                                                             | 96.4 ms: 1.26x slower                                  |
| Geometric mean | (ref)                                                               | 1.08x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_list          | 2.86 us                                                             | 2.80 us: 1.02x faster                                  |
| unpickle_list        | 2.64 us                                                             | 2.69 us: 1.02x slower                                  |
| pickle               | 7.21 us                                                             | 7.35 us: 1.02x slower                                  |
| unpickle             | 9.68 us                                                             | 9.89 us: 1.02x slower                                  |
| json_loads           | 16.1 us                                                             | 16.9 us: 1.05x slower                                  |
| xml_etree_parse      | 99.6 ms                                                             | 106 ms: 1.07x slower                                   |
| json_dumps           | 7.67 ms                                                             | 8.40 ms: 1.09x slower                                  |
| xml_etree_iterparse  | 65.6 ms                                                             | 72.3 ms: 1.10x slower                                  |
| xml_etree_generate   | 48.4 ms                                                             | 54.2 ms: 1.12x slower                                  |
| unpickle_pure_python | 159 us                                                              | 203 us: 1.28x slower                                   |
| xml_etree_process    | 35.1 ms                                                             | 44.8 ms: 1.28x slower                                  |
| pickle_pure_python   | 200 us                                                              | 283 us: 1.42x slower                                   |
| Geometric mean       | (ref)                                                               | 1.10x slower                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 7.24 ms                                                             | 8.88 ms: 1.23x slower                                  |
| python_startup         | 9.19 ms                                                             | 11.9 ms: 1.30x slower                                  |
| Geometric mean         | (ref)                                                               | 1.26x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                             | 18.4 ms: 1.20x slower                                  |
| genshi_xml      | 30.5 ms                                                             | 37.2 ms: 1.22x slower                                  |
| mako            | 8.40 ms                                                             | 10.5 ms: 1.25x slower                                  |
| django_template | 21.1 ms                                                             | 27.3 ms: 1.29x slower                                  |
| Geometric mean  | (ref)                                                               | 1.24x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| coverage                | 58.4 ms                                                             | 42.0 ms: 1.39x faster                                  |
| regex_effbot            | 2.63 ms                                                             | 2.46 ms: 1.07x faster                                  |
| bench_mp_pool           | 41.4 ms                                                             | 39.7 ms: 1.04x faster                                  |
| pickle_list             | 2.86 us                                                             | 2.80 us: 1.02x faster                                  |
| unpickle_list           | 2.64 us                                                             | 2.69 us: 1.02x slower                                  |
| pickle                  | 7.21 us                                                             | 7.35 us: 1.02x slower                                  |
| unpickle                | 9.68 us                                                             | 9.89 us: 1.02x slower                                  |
| json_loads              | 16.1 us                                                             | 16.9 us: 1.05x slower                                  |
| meteor_contest          | 73.9 ms                                                             | 78.1 ms: 1.06x slower                                  |
| regex_v8                | 16.5 ms                                                             | 17.6 ms: 1.07x slower                                  |
| regex_dna               | 151 ms                                                              | 162 ms: 1.07x slower                                   |
| xml_etree_parse         | 99.6 ms                                                             | 106 ms: 1.07x slower                                   |
| telco                   | 3.39 ms                                                             | 3.63 ms: 1.07x slower                                  |
| mdp                     | 1.54 sec                                                            | 1.66 sec: 1.08x slower                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                             | 3.46 ms: 1.08x slower                                  |
| json                    | 2.83 ms                                                             | 3.08 ms: 1.09x slower                                  |
| json_dumps              | 7.67 ms                                                             | 8.40 ms: 1.09x slower                                  |
| sympy_sum               | 85.5 ms                                                             | 93.6 ms: 1.09x slower                                  |
| xml_etree_iterparse     | 65.6 ms                                                             | 72.3 ms: 1.10x slower                                  |
| 2to3                    | 181 ms                                                              | 201 ms: 1.11x slower                                   |
| xml_etree_generate      | 48.4 ms                                                             | 54.2 ms: 1.12x slower                                  |
| sympy_str               | 151 ms                                                              | 169 ms: 1.12x slower                                   |
| unpack_sequence         | 33.1 ns                                                             | 37.4 ns: 1.13x slower                                  |
| coroutines              | 17.8 ms                                                             | 20.2 ms: 1.14x slower                                  |
| sympy_expand            | 242 ms                                                              | 275 ms: 1.14x slower                                   |
| sqlite_synth            | 1.29 us                                                             | 1.47 us: 1.14x slower                                  |
| nqueens                 | 59.5 ms                                                             | 68.2 ms: 1.15x slower                                  |
| sqlglot_normalize       | 171 ms                                                              | 196 ms: 1.15x slower                                   |
| scimark_fft             | 201 ms                                                              | 230 ms: 1.15x slower                                   |
| generators              | 28.4 ms                                                             | 32.7 ms: 1.15x slower                                  |
| sympy_integrate         | 11.5 ms                                                             | 13.3 ms: 1.16x slower                                  |
| pylint                  | 265 ms                                                              | 307 ms: 1.16x slower                                   |
| bench_thread_pool       | 457 us                                                              | 546 us: 1.19x slower                                   |
| aiohttp                 | 1.06 ms                                                             | 1.27 ms: 1.20x slower                                  |
| async_generators        | 195 ms                                                              | 234 ms: 1.20x slower                                   |
| genshi_text             | 15.3 ms                                                             | 18.4 ms: 1.20x slower                                  |
| sqlalchemy_declarative  | 62.4 ms                                                             | 74.9 ms: 1.20x slower                                  |
| flaskblogging           | 2.29 ms                                                             | 2.75 ms: 1.20x slower                                  |
| gunicorn                | 1.12 ms                                                             | 1.35 ms: 1.20x slower                                  |
| fannkuch                | 262 ms                                                              | 317 ms: 1.21x slower                                   |
| sqlglot_optimize        | 31.3 ms                                                             | 38.0 ms: 1.21x slower                                  |
| docutils                | 1.46 sec                                                            | 1.78 sec: 1.22x slower                                 |
| genshi_xml              | 30.5 ms                                                             | 37.2 ms: 1.22x slower                                  |
| python_startup_no_site  | 7.24 ms                                                             | 8.88 ms: 1.23x slower                                  |
| sqlalchemy_imperative   | 7.22 ms                                                             | 8.89 ms: 1.23x slower                                  |
| mako                    | 8.40 ms                                                             | 10.5 ms: 1.25x slower                                  |
| deepcopy_reduce         | 1.90 us                                                             | 2.37 us: 1.25x slower                                  |
| chameleon               | 4.61 ms                                                             | 5.79 ms: 1.26x slower                                  |
| regex_compile           | 76.3 ms                                                             | 96.4 ms: 1.26x slower                                  |
| deepcopy                | 222 us                                                              | 281 us: 1.27x slower                                   |
| async_tree_cpu_io_mixed | 528 ms                                                              | 669 ms: 1.27x slower                                   |
| unpickle_pure_python    | 159 us                                                              | 203 us: 1.28x slower                                   |
| html5lib                | 34.7 ms                                                             | 44.2 ms: 1.28x slower                                  |
| dulwich_log             | 29.1 ms                                                             | 37.1 ms: 1.28x slower                                  |
| xml_etree_process       | 35.1 ms                                                             | 44.8 ms: 1.28x slower                                  |
| pprint_pformat          | 953 ms                                                              | 1.23 sec: 1.29x slower                                 |
| django_template         | 21.1 ms                                                             | 27.3 ms: 1.29x slower                                  |
| python_startup          | 9.19 ms                                                             | 11.9 ms: 1.30x slower                                  |
| pprint_safe_repr        | 467 ms                                                              | 606 ms: 1.30x slower                                   |
| tornado_http            | 70.6 ms                                                             | 91.5 ms: 1.30x slower                                  |
| deepcopy_memo           | 26.2 us                                                             | 34.4 us: 1.32x slower                                  |
| spectral_norm           | 72.7 ms                                                             | 95.8 ms: 1.32x slower                                  |
| pycparser               | 694 ms                                                              | 916 ms: 1.32x slower                                   |
| logging_format          | 3.73 us                                                             | 4.97 us: 1.33x slower                                  |
| logging_simple          | 3.47 us                                                             | 4.63 us: 1.34x slower                                  |
| hexiom                  | 4.73 ms                                                             | 6.32 ms: 1.34x slower                                  |
| thrift                  | 429 us                                                              | 580 us: 1.35x slower                                   |
| chaos                   | 49.3 ms                                                             | 66.7 ms: 1.35x slower                                  |
| pathlib                 | 20.6 ms                                                             | 28.8 ms: 1.40x slower                                  |
| float                   | 51.7 ms                                                             | 72.4 ms: 1.40x slower                                  |
| sqlglot_transpile       | 1.11 ms                                                             | 1.57 ms: 1.42x slower                                  |
| pickle_pure_python      | 200 us                                                              | 283 us: 1.42x slower                                   |
| async_tree_none         | 281 ms                                                              | 400 ms: 1.42x slower                                   |
| nbody                   | 65.2 ms                                                             | 93.3 ms: 1.43x slower                                  |
| sqlglot_parse           | 948 us                                                              | 1.37 ms: 1.44x slower                                  |
| pyflate                 | 313 ms                                                              | 453 ms: 1.45x slower                                   |
| async_tree_io           | 696 ms                                                              | 1.02 sec: 1.46x slower                                 |
| crypto_pyaes            | 51.7 ms                                                             | 78.1 ms: 1.51x slower                                  |
| go                      | 109 ms                                                              | 165 ms: 1.51x slower                                   |
| scimark_lu              | 72.2 ms                                                             | 109 ms: 1.51x slower                                   |
| scimark_sor             | 83.3 ms                                                             | 126 ms: 1.51x slower                                   |
| scimark_monte_carlo     | 46.9 ms                                                             | 72.5 ms: 1.54x slower                                  |
| async_tree_memoization  | 317 ms                                                              | 490 ms: 1.55x slower                                   |
| raytrace                | 207 ms                                                              | 325 ms: 1.57x slower                                   |
| richards                | 32.7 ms                                                             | 51.4 ms: 1.57x slower                                  |
| logging_silent          | 67.4 ns                                                             | 119 ns: 1.77x slower                                   |
| deltablue               | 2.82 ms                                                             | 5.14 ms: 1.82x slower                                  |
| Geometric mean          | (ref)                                                               | 1.23x slower                                           |

Benchmark hidden because not significant (2): pickle_dict, pidigits
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
