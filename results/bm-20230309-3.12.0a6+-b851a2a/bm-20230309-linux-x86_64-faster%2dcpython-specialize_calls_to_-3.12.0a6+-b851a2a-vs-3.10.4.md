
# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_calls_to_
- machine: linux-x86_64
- commit hash: b851a2a
- commit date: 2023-03-09
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.67 ms: 1.37x faster                                                            |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 62.3 ms: 1.38x faster                                                            |
| tornado_http   | 128 ms                                                 | 95.5 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.0 ms: 1.53x faster                                                            |
| float          | 109 ms                                                 | 74.1 ms: 1.47x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                            |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.9 ms: 1.33x faster                                                            |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 81.2 ms: 1.16x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.25 us: 1.11x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                             |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                            |
| unpickle_list        | 4.92 us                                                | 5.00 us: 1.02x slower                                                            |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                                            |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.15x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.03 ms: 1.56x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                            |
| genshi_text     | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                            |
| django_template | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.3 ms: 2.52x faster                                                            |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                            |
| logging_silent          | 176 ns                                                 | 94.6 ns: 1.87x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 513 ms: 1.78x faster                                                             |
| raytrace                | 467 ms                                                 | 267 ms: 1.75x faster                                                             |
| richards                | 75.2 ms                                                | 43.5 ms: 1.73x faster                                                            |
| pyflate                 | 676 ms                                                 | 411 ms: 1.65x faster                                                             |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 66.8 ms: 1.62x faster                                                            |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.61x faster                                                            |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 74.7 ms: 1.56x faster                                                            |
| python_startup          | 14.1 ms                                                | 9.03 ms: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 96.9 ms: 1.54x faster                                                            |
| nbody                   | 144 ms                                                 | 94.0 ms: 1.53x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                            |
| hexiom                  | 9.43 ms                                                | 6.24 ms: 1.51x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                                             |
| float                   | 109 ms                                                 | 74.1 ms: 1.47x faster                                                            |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                            |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 41.5 ns: 1.43x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                           |
| genshi_text             | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.41x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.79 us: 1.40x faster                                                            |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                                            |
| django_template         | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 690 ms: 1.38x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.3 ms: 1.38x faster                                                            |
| chameleon               | 9.17 ms                                                | 6.67 ms: 1.37x faster                                                            |
| coroutines              | 31.6 ms                                                | 23.0 ms: 1.37x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                           |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                             |
| tornado_http            | 128 ms                                                 | 95.5 ms: 1.34x faster                                                            |
| scimark_fft             | 421 ms                                                 | 315 ms: 1.34x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 55.9 ms: 1.33x faster                                                            |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                                             |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.32x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                                           |
| genshi_xml              | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                            |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| deepcopy                | 438 us                                                 | 334 us: 1.31x faster                                                             |
| thrift                  | 1.03 ms                                                | 790 us: 1.31x faster                                                             |
| fannkuch                | 488 ms                                                 | 373 ms: 1.31x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                            |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 664 ms: 1.29x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed | 949 ms                                                 | 747 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 3.01 us: 1.26x faster                                                            |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                                            |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                           |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                             |
| bench_thread_pool       | 946 us                                                 | 790 us: 1.20x faster                                                             |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                            |
| dulwich_log             | 75.8 ms                                                | 63.9 ms: 1.19x faster                                                            |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.18x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.6 ms: 1.17x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                            |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 81.2 ms: 1.16x faster                                                            |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.15x faster                                                             |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                                             |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.11x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.25 us: 1.11x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.64 us: 1.11x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.48 sec: 1.10x faster                                                           |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                            |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                             |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                             |
| async_generators        | 426 ms                                                 | 403 ms: 1.06x faster                                                             |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                             |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                            |
| telco                   | 6.73 ms                                                | 6.61 ms: 1.02x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| unpickle_list           | 4.92 us                                                | 5.00 us: 1.02x slower                                                            |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                                            |
| regex_effbot            | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 3.85 ms: 1.09x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                            |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.15x slower                                                            |
| dask                    | 436 ms                                                 | 513 ms: 1.18x slower                                                             |
| coverage                | 74.7 ms                                                | 95.1 ms: 1.27x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a6+-b851a2a/bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a.json: comprehensions
