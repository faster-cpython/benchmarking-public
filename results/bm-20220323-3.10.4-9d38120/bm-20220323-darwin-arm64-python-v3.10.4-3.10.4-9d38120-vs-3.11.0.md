
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: darwin-arm64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.21x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 201 ms: 1.25x slower                                   |
| chameleon      | 4.55 ms                                                             | 5.79 ms: 1.27x slower                                  |
| docutils       | 1.47 sec                                                            | 1.78 sec: 1.21x slower                                 |
| html5lib       | 34.8 ms                                                             | 44.2 ms: 1.27x slower                                  |
| tornado_http   | 71.5 ms                                                             | 91.5 ms: 1.28x slower                                  |
| Geometric mean | (ref)                                                               | 1.26x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 281 ms                                                              | 282 ms: 1.01x slower                                   |
| float          | 53.0 ms                                                             | 72.4 ms: 1.37x slower                                  |
| nbody          | 65.5 ms                                                             | 93.3 ms: 1.43x slower                                  |
| Geometric mean | (ref)                                                               | 1.25x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.46 ms: 1.07x faster                                  |
| regex_dna      | 151 ms                                                              | 162 ms: 1.07x slower                                   |
| regex_v8       | 16.1 ms                                                             | 17.6 ms: 1.09x slower                                  |
| regex_compile  | 76.6 ms                                                             | 96.4 ms: 1.26x slower                                  |
| Geometric mean | (ref)                                                               | 1.08x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_list          | 2.83 us                                                             | 2.80 us: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                             | 17.9 us: 1.00x slower                                  |
| unpickle_list        | 2.63 us                                                             | 2.69 us: 1.02x slower                                  |
| unpickle             | 9.66 us                                                             | 9.89 us: 1.02x slower                                  |
| pickle               | 7.17 us                                                             | 7.35 us: 1.03x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                             | 72.3 ms: 1.04x slower                                  |
| json_loads           | 16.0 us                                                             | 16.9 us: 1.05x slower                                  |
| json_dumps           | 7.59 ms                                                             | 8.40 ms: 1.11x slower                                  |
| xml_etree_generate   | 48.2 ms                                                             | 54.2 ms: 1.12x slower                                  |
| xml_etree_process    | 35.0 ms                                                             | 44.8 ms: 1.28x slower                                  |
| unpickle_pure_python | 158 us                                                              | 203 us: 1.28x slower                                   |
| pickle_pure_python   | 198 us                                                              | 283 us: 1.43x slower                                   |
| Geometric mean       | (ref)                                                               | 1.10x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                             | 8.88 ms: 1.13x faster                                  |
| python_startup         | 12.3 ms                                                             | 11.9 ms: 1.03x faster                                  |
| Geometric mean         | (ref)                                                               | 1.08x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                             | 18.4 ms: 1.20x slower                                  |
| genshi_xml      | 29.9 ms                                                             | 37.2 ms: 1.24x slower                                  |
| mako            | 8.42 ms                                                             | 10.5 ms: 1.25x slower                                  |
| django_template | 21.1 ms                                                             | 27.3 ms: 1.29x slower                                  |
| Geometric mean  | (ref)                                                               | 1.24x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| coverage                | 58.4 ms                                                             | 42.0 ms: 1.39x faster                                  |
| python_startup_no_site  | 10.1 ms                                                             | 8.88 ms: 1.13x faster                                  |
| bench_mp_pool           | 43.8 ms                                                             | 39.7 ms: 1.10x faster                                  |
| regex_effbot            | 2.63 ms                                                             | 2.46 ms: 1.07x faster                                  |
| python_startup          | 12.3 ms                                                             | 11.9 ms: 1.03x faster                                  |
| pickle_list             | 2.83 us                                                             | 2.80 us: 1.01x faster                                  |
| gc_traversal            | 2.41 ms                                                             | 2.39 ms: 1.01x faster                                  |
| pickle_dict             | 17.9 us                                                             | 17.9 us: 1.00x slower                                  |
| pidigits                | 281 ms                                                              | 282 ms: 1.01x slower                                   |
| pathlib                 | 28.3 ms                                                             | 28.8 ms: 1.02x slower                                  |
| unpickle_list           | 2.63 us                                                             | 2.69 us: 1.02x slower                                  |
| unpickle                | 9.66 us                                                             | 9.89 us: 1.02x slower                                  |
| pickle                  | 7.17 us                                                             | 7.35 us: 1.03x slower                                  |
| asyncio_tcp             | 651 ms                                                              | 670 ms: 1.03x slower                                   |
| xml_etree_iterparse     | 69.2 ms                                                             | 72.3 ms: 1.04x slower                                  |
| json_loads              | 16.0 us                                                             | 16.9 us: 1.05x slower                                  |
| meteor_contest          | 73.3 ms                                                             | 78.1 ms: 1.06x slower                                  |
| regex_dna               | 151 ms                                                              | 162 ms: 1.07x slower                                   |
| telco                   | 3.40 ms                                                             | 3.63 ms: 1.07x slower                                  |
| mdp                     | 1.54 sec                                                            | 1.66 sec: 1.08x slower                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.46 ms: 1.08x slower                                  |
| sympy_sum               | 86.0 ms                                                             | 93.6 ms: 1.09x slower                                  |
| regex_v8                | 16.1 ms                                                             | 17.6 ms: 1.09x slower                                  |
| nqueens                 | 62.4 ms                                                             | 68.2 ms: 1.09x slower                                  |
| comprehensions          | 16.1 us                                                             | 17.6 us: 1.09x slower                                  |
| json_dumps              | 7.59 ms                                                             | 8.40 ms: 1.11x slower                                  |
| json                    | 2.77 ms                                                             | 3.08 ms: 1.11x slower                                  |
| unpack_sequence         | 33.5 ns                                                             | 37.4 ns: 1.11x slower                                  |
| sympy_str               | 151 ms                                                              | 169 ms: 1.12x slower                                   |
| xml_etree_generate      | 48.2 ms                                                             | 54.2 ms: 1.12x slower                                  |
| sympy_expand            | 243 ms                                                              | 275 ms: 1.13x slower                                   |
| pylint                  | 271 ms                                                              | 307 ms: 1.14x slower                                   |
| flaskblogging           | 2.42 ms                                                             | 2.75 ms: 1.14x slower                                  |
| coroutines              | 17.7 ms                                                             | 20.2 ms: 1.14x slower                                  |
| generators              | 28.6 ms                                                             | 32.7 ms: 1.14x slower                                  |
| sqlglot_normalize       | 171 ms                                                              | 196 ms: 1.15x slower                                   |
| sqlite_synth            | 1.28 us                                                             | 1.47 us: 1.15x slower                                  |
| scimark_fft             | 200 ms                                                              | 230 ms: 1.15x slower                                   |
| bench_thread_pool       | 474 us                                                              | 546 us: 1.15x slower                                   |
| sympy_integrate         | 11.5 ms                                                             | 13.3 ms: 1.16x slower                                  |
| dask                    | 226 ms                                                              | 265 ms: 1.17x slower                                   |
| sqlalchemy_declarative  | 62.6 ms                                                             | 74.9 ms: 1.20x slower                                  |
| async_generators        | 195 ms                                                              | 234 ms: 1.20x slower                                   |
| genshi_text             | 15.3 ms                                                             | 18.4 ms: 1.20x slower                                  |
| gunicorn                | 1.12 ms                                                             | 1.35 ms: 1.20x slower                                  |
| aiohttp                 | 1.05 ms                                                             | 1.27 ms: 1.21x slower                                  |
| docutils                | 1.47 sec                                                            | 1.78 sec: 1.21x slower                                 |
| sqlglot_optimize        | 31.2 ms                                                             | 38.0 ms: 1.22x slower                                  |
| create_gc_cycles        | 722 us                                                              | 880 us: 1.22x slower                                   |
| fannkuch                | 260 ms                                                              | 317 ms: 1.22x slower                                   |
| sqlalchemy_imperative   | 7.26 ms                                                             | 8.89 ms: 1.22x slower                                  |
| mypy2                   | 249 ms                                                              | 307 ms: 1.23x slower                                   |
| genshi_xml              | 29.9 ms                                                             | 37.2 ms: 1.24x slower                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.37 us: 1.24x slower                                  |
| mako                    | 8.42 ms                                                             | 10.5 ms: 1.25x slower                                  |
| dulwich_log             | 29.7 ms                                                             | 37.1 ms: 1.25x slower                                  |
| 2to3                    | 161 ms                                                              | 201 ms: 1.25x slower                                   |
| async_tree_cpu_io_mixed | 534 ms                                                              | 669 ms: 1.25x slower                                   |
| deepcopy                | 224 us                                                              | 281 us: 1.26x slower                                   |
| regex_compile           | 76.6 ms                                                             | 96.4 ms: 1.26x slower                                  |
| html5lib                | 34.8 ms                                                             | 44.2 ms: 1.27x slower                                  |
| chameleon               | 4.55 ms                                                             | 5.79 ms: 1.27x slower                                  |
| xml_etree_process       | 35.0 ms                                                             | 44.8 ms: 1.28x slower                                  |
| tornado_http            | 71.5 ms                                                             | 91.5 ms: 1.28x slower                                  |
| unpickle_pure_python    | 158 us                                                              | 203 us: 1.28x slower                                   |
| django_template         | 21.1 ms                                                             | 27.3 ms: 1.29x slower                                  |
| pprint_pformat          | 946 ms                                                              | 1.23 sec: 1.30x slower                                 |
| pprint_safe_repr        | 463 ms                                                              | 606 ms: 1.31x slower                                   |
| deepcopy_memo           | 26.3 us                                                             | 34.4 us: 1.31x slower                                  |
| logging_format          | 3.77 us                                                             | 4.97 us: 1.32x slower                                  |
| pycparser               | 695 ms                                                              | 916 ms: 1.32x slower                                   |
| spectral_norm           | 72.5 ms                                                             | 95.8 ms: 1.32x slower                                  |
| logging_simple          | 3.49 us                                                             | 4.63 us: 1.32x slower                                  |
| hexiom                  | 4.73 ms                                                             | 6.32 ms: 1.33x slower                                  |
| thrift                  | 431 us                                                              | 580 us: 1.35x slower                                   |
| chaos                   | 49.4 ms                                                             | 66.7 ms: 1.35x slower                                  |
| float                   | 53.0 ms                                                             | 72.4 ms: 1.37x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                             | 1.57 ms: 1.41x slower                                  |
| async_tree_none         | 285 ms                                                              | 400 ms: 1.41x slower                                   |
| nbody                   | 65.5 ms                                                             | 93.3 ms: 1.43x slower                                  |
| pickle_pure_python      | 198 us                                                              | 283 us: 1.43x slower                                   |
| sqlglot_parse           | 956 us                                                              | 1.37 ms: 1.43x slower                                  |
| async_tree_io           | 707 ms                                                              | 1.02 sec: 1.44x slower                                 |
| async_tree_memoization  | 338 ms                                                              | 490 ms: 1.45x slower                                   |
| pyflate                 | 309 ms                                                              | 453 ms: 1.46x slower                                   |
| crypto_pyaes            | 51.8 ms                                                             | 78.1 ms: 1.51x slower                                  |
| scimark_lu              | 72.2 ms                                                             | 109 ms: 1.51x slower                                   |
| go                      | 109 ms                                                              | 165 ms: 1.52x slower                                   |
| scimark_sor             | 82.9 ms                                                             | 126 ms: 1.52x slower                                   |
| scimark_monte_carlo     | 46.5 ms                                                             | 72.5 ms: 1.56x slower                                  |
| raytrace                | 207 ms                                                              | 325 ms: 1.57x slower                                   |
| richards                | 32.2 ms                                                             | 51.4 ms: 1.60x slower                                  |
| logging_silent          | 68.0 ns                                                             | 119 ns: 1.76x slower                                   |
| deltablue               | 2.81 ms                                                             | 5.14 ms: 1.83x slower                                  |
| Geometric mean          | (ref)                                                               | 1.21x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse
