
# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_calls_to_
- machine: linux-x86_64
- commit hash: b851a2a
- commit date: 2023-03-09
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.67 ms: 1.36x faster                                                            |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                           |
| html5lib       | 85.9 ms                                                | 62.3 ms: 1.38x faster                                                            |
| tornado_http   | 127 ms                                                 | 95.5 ms: 1.33x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.0 ms: 1.51x faster                                                            |
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                            |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.37 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.47 ms: 1.43x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 55.9 ms: 1.34x faster                                                            |
| json_loads           | 28.8 us                                                | 24.1 us: 1.19x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                                            |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                            |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                            |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.03 ms: 1.57x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                            |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                            |
| django_template | 45.9 ms                                                | 33.4 ms: 1.37x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.3 ms: 2.53x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                            |
| logging_silent          | 175 ns                                                 | 94.6 ns: 1.85x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 513 ms: 1.80x faster                                                             |
| raytrace                | 464 ms                                                 | 267 ms: 1.74x faster                                                             |
| richards                | 74.9 ms                                                | 43.5 ms: 1.72x faster                                                            |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                             |
| pyflate                 | 673 ms                                                 | 411 ms: 1.64x faster                                                             |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.62x faster                                                            |
| scimark_monte_carlo     | 108 ms                                                 | 66.8 ms: 1.62x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.59x faster                                                            |
| python_startup          | 14.2 ms                                                | 9.03 ms: 1.57x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 41.5 ns: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 96.9 ms: 1.55x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                            |
| hexiom                  | 9.53 ms                                                | 6.24 ms: 1.53x faster                                                            |
| nbody                   | 142 ms                                                 | 94.0 ms: 1.51x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                             |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                                            |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                             |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.47 ms: 1.43x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                           |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.79 us: 1.39x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 690 ms: 1.38x faster                                                             |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                            |
| html5lib                | 85.9 ms                                                | 62.3 ms: 1.38x faster                                                            |
| django_template         | 45.9 ms                                                | 33.4 ms: 1.37x faster                                                            |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                             |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.67 ms: 1.36x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                                           |
| scimark_fft             | 424 ms                                                 | 315 ms: 1.35x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 55.9 ms: 1.34x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                                            |
| tornado_http            | 127 ms                                                 | 95.5 ms: 1.33x faster                                                            |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                             |
| deepcopy                | 442 us                                                 | 334 us: 1.32x faster                                                             |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                            |
| thrift                  | 1.03 ms                                                | 790 us: 1.31x faster                                                             |
| fannkuch                | 486 ms                                                 | 373 ms: 1.30x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                           |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 664 ms: 1.29x faster                                                             |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.01 us: 1.27x faster                                                            |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                                            |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                           |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                             |
| json_loads              | 28.8 us                                                | 24.1 us: 1.19x faster                                                            |
| dulwich_log             | 75.9 ms                                                | 63.9 ms: 1.19x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                            |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                            |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                            |
| sympy_str               | 328 ms                                                 | 287 ms: 1.15x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                                           |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                             |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                             |
| djangocms               | 35.9 us                                                | 32.7 us: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                             |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                             |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                                            |
| async_generators        | 425 ms                                                 | 403 ms: 1.05x faster                                                             |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.85 ms: 1.00x slower                                                            |
| telco                   | 6.54 ms                                                | 6.61 ms: 1.01x slower                                                            |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                            |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.37 ms: 1.04x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                            |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                            |
| dask                    | 423 ms                                                 | 513 ms: 1.21x slower                                                             |
| coverage                | 72.8 ms                                                | 95.1 ms: 1.31x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
