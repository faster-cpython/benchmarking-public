
# Results vs. 3.10.4

- fork: python
- ref: deaf509e8fc6e0363bd6
- machine: darwin-arm64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 181 ms: 1.11x faster                                                |
| chameleon      | 5.79 ms                                                | 4.61 ms: 1.26x faster                                               |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                              |
| html5lib       | 44.2 ms                                                | 34.7 ms: 1.28x faster                                               |
| tornado_http   | 91.5 ms                                                | 70.6 ms: 1.30x faster                                               |
| Geometric mean | (ref)                                                  | 1.23x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.2 ms: 1.43x faster                                               |
| float          | 72.4 ms                                                | 51.7 ms: 1.40x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.3 ms: 1.26x faster                                               |
| regex_dna      | 162 ms                                                 | 151 ms: 1.07x faster                                                |
| regex_v8       | 17.6 ms                                                | 16.5 ms: 1.07x faster                                               |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 200 us: 1.42x faster                                                |
| xml_etree_process    | 44.8 ms                                                | 35.1 ms: 1.28x faster                                               |
| unpickle_pure_python | 203 us                                                 | 159 us: 1.28x faster                                                |
| xml_etree_generate   | 54.2 ms                                                | 48.4 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 72.3 ms                                                | 65.6 ms: 1.10x faster                                               |
| json_dumps           | 8.40 ms                                                | 7.67 ms: 1.09x faster                                               |
| xml_etree_parse      | 106 ms                                                 | 99.6 ms: 1.07x faster                                               |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                               |
| unpickle             | 9.89 us                                                | 9.68 us: 1.02x faster                                               |
| pickle               | 7.35 us                                                | 7.21 us: 1.02x faster                                               |
| unpickle_list        | 2.69 us                                                | 2.64 us: 1.02x faster                                               |
| pickle_list          | 2.80 us                                                | 2.86 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.19 ms: 1.30x faster                                               |
| python_startup_no_site | 8.88 ms                                                | 7.24 ms: 1.23x faster                                               |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.1 ms: 1.29x faster                                               |
| mako            | 10.5 ms                                                | 8.40 ms: 1.25x faster                                               |
| genshi_xml      | 37.2 ms                                                | 30.5 ms: 1.22x faster                                               |
| genshi_text     | 18.4 ms                                                | 15.3 ms: 1.20x faster                                               |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.82 ms: 1.82x faster                                               |
| logging_silent          | 119 ns                                                 | 67.4 ns: 1.77x faster                                               |
| richards                | 51.4 ms                                                | 32.7 ms: 1.57x faster                                               |
| raytrace                | 325 ms                                                 | 207 ms: 1.57x faster                                                |
| async_tree_memoization  | 490 ms                                                 | 317 ms: 1.55x faster                                                |
| scimark_monte_carlo     | 72.5 ms                                                | 46.9 ms: 1.54x faster                                               |
| scimark_sor             | 126 ms                                                 | 83.3 ms: 1.51x faster                                               |
| scimark_lu              | 109 ms                                                 | 72.2 ms: 1.51x faster                                               |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                |
| crypto_pyaes            | 78.1 ms                                                | 51.7 ms: 1.51x faster                                               |
| async_tree_io           | 1.02 sec                                               | 696 ms: 1.46x faster                                                |
| pyflate                 | 453 ms                                                 | 313 ms: 1.45x faster                                                |
| sqlglot_parse           | 1.37 ms                                                | 948 us: 1.44x faster                                                |
| nbody                   | 93.3 ms                                                | 65.2 ms: 1.43x faster                                               |
| async_tree_none         | 400 ms                                                 | 281 ms: 1.42x faster                                                |
| pickle_pure_python      | 283 us                                                 | 200 us: 1.42x faster                                                |
| sqlglot_transpile       | 1.57 ms                                                | 1.11 ms: 1.42x faster                                               |
| float                   | 72.4 ms                                                | 51.7 ms: 1.40x faster                                               |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.40x faster                                               |
| chaos                   | 66.7 ms                                                | 49.3 ms: 1.35x faster                                               |
| thrift                  | 580 us                                                 | 429 us: 1.35x faster                                                |
| hexiom                  | 6.32 ms                                                | 4.73 ms: 1.34x faster                                               |
| logging_simple          | 4.63 us                                                | 3.47 us: 1.34x faster                                               |
| logging_format          | 4.97 us                                                | 3.73 us: 1.33x faster                                               |
| pycparser               | 916 ms                                                 | 694 ms: 1.32x faster                                                |
| spectral_norm           | 95.8 ms                                                | 72.7 ms: 1.32x faster                                               |
| deepcopy_memo           | 34.4 us                                                | 26.2 us: 1.32x faster                                               |
| tornado_http            | 91.5 ms                                                | 70.6 ms: 1.30x faster                                               |
| pprint_safe_repr        | 606 ms                                                 | 467 ms: 1.30x faster                                                |
| python_startup          | 11.9 ms                                                | 9.19 ms: 1.30x faster                                               |
| django_template         | 27.3 ms                                                | 21.1 ms: 1.29x faster                                               |
| pprint_pformat          | 1.23 sec                                               | 953 ms: 1.29x faster                                                |
| xml_etree_process       | 44.8 ms                                                | 35.1 ms: 1.28x faster                                               |
| dulwich_log             | 37.1 ms                                                | 29.1 ms: 1.28x faster                                               |
| html5lib                | 44.2 ms                                                | 34.7 ms: 1.28x faster                                               |
| unpickle_pure_python    | 203 us                                                 | 159 us: 1.28x faster                                                |
| async_tree_cpu_io_mixed | 669 ms                                                 | 528 ms: 1.27x faster                                                |
| deepcopy                | 281 us                                                 | 222 us: 1.27x faster                                                |
| regex_compile           | 96.4 ms                                                | 76.3 ms: 1.26x faster                                               |
| chameleon               | 5.79 ms                                                | 4.61 ms: 1.26x faster                                               |
| deepcopy_reduce         | 2.37 us                                                | 1.90 us: 1.25x faster                                               |
| mako                    | 10.5 ms                                                | 8.40 ms: 1.25x faster                                               |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.22 ms: 1.23x faster                                               |
| python_startup_no_site  | 8.88 ms                                                | 7.24 ms: 1.23x faster                                               |
| genshi_xml              | 37.2 ms                                                | 30.5 ms: 1.22x faster                                               |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                              |
| sqlglot_optimize        | 38.0 ms                                                | 31.3 ms: 1.21x faster                                               |
| fannkuch                | 317 ms                                                 | 262 ms: 1.21x faster                                                |
| gunicorn                | 1.35 ms                                                | 1.12 ms: 1.20x faster                                               |
| flaskblogging           | 2.75 ms                                                | 2.29 ms: 1.20x faster                                               |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.4 ms: 1.20x faster                                               |
| genshi_text             | 18.4 ms                                                | 15.3 ms: 1.20x faster                                               |
| async_generators        | 234 ms                                                 | 195 ms: 1.20x faster                                                |
| aiohttp                 | 1.27 ms                                                | 1.06 ms: 1.20x faster                                               |
| bench_thread_pool       | 546 us                                                 | 457 us: 1.19x faster                                                |
| pylint                  | 307 ms                                                 | 265 ms: 1.16x faster                                                |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.16x faster                                               |
| generators              | 32.7 ms                                                | 28.4 ms: 1.15x faster                                               |
| scimark_fft             | 230 ms                                                 | 201 ms: 1.15x faster                                                |
| sqlglot_normalize       | 196 ms                                                 | 171 ms: 1.15x faster                                                |
| nqueens                 | 68.2 ms                                                | 59.5 ms: 1.15x faster                                               |
| sqlite_synth            | 1.47 us                                                | 1.29 us: 1.14x faster                                               |
| sympy_expand            | 275 ms                                                 | 242 ms: 1.14x faster                                                |
| coroutines              | 20.2 ms                                                | 17.8 ms: 1.14x faster                                               |
| unpack_sequence         | 37.4 ns                                                | 33.1 ns: 1.13x faster                                               |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                                |
| xml_etree_generate      | 54.2 ms                                                | 48.4 ms: 1.12x faster                                               |
| 2to3                    | 201 ms                                                 | 181 ms: 1.11x faster                                                |
| xml_etree_iterparse     | 72.3 ms                                                | 65.6 ms: 1.10x faster                                               |
| sympy_sum               | 93.6 ms                                                | 85.5 ms: 1.09x faster                                               |
| json_dumps              | 8.40 ms                                                | 7.67 ms: 1.09x faster                                               |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.20 ms: 1.08x faster                                               |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                              |
| telco                   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                               |
| xml_etree_parse         | 106 ms                                                 | 99.6 ms: 1.07x faster                                               |
| regex_dna               | 162 ms                                                 | 151 ms: 1.07x faster                                                |
| regex_v8                | 17.6 ms                                                | 16.5 ms: 1.07x faster                                               |
| meteor_contest          | 78.1 ms                                                | 73.9 ms: 1.06x faster                                               |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                               |
| unpickle                | 9.89 us                                                | 9.68 us: 1.02x faster                                               |
| pickle                  | 7.35 us                                                | 7.21 us: 1.02x faster                                               |
| unpickle_list           | 2.69 us                                                | 2.64 us: 1.02x faster                                               |
| pickle_list             | 2.80 us                                                | 2.86 us: 1.02x slower                                               |
| bench_mp_pool           | 39.7 ms                                                | 41.4 ms: 1.04x slower                                               |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                               |
| coverage                | 42.0 ms                                                | 58.4 ms: 1.39x slower                                               |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                        |

Benchmark hidden because not significant (2): pidigits, pickle_dict
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: mypy
