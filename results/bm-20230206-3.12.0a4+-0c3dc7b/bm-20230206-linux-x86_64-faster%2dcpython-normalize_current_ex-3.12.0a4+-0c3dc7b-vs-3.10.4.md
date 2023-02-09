
# Results vs. 3.10.4

- fork: faster-cpython
- ref: normalize_current_ex
- machine: linux-x86_64
- commit hash: 0c3dc7b
- commit date: 2023-02-06
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                             |
| chameleon      | 8.86 ms                                                | 6.51 ms: 1.36x faster                                                            |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                           |
| html5lib       | 85.8 ms                                                | 61.1 ms: 1.40x faster                                                            |
| tornado_http   | 128 ms                                                 | 94.4 ms: 1.36x faster                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.5 ms: 1.49x faster                                                            |
| nbody          | 136 ms                                                 | 94.6 ms: 1.44x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                             |
| regex_effbot   | 3.21 ms                                                | 3.36 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 284 us: 1.59x faster                                                             |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                                            |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                                            |
| xml_etree_generate   | 93.3 ms                                                | 79.7 ms: 1.17x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                             |
| pickle_list          | 4.50 us                                                | 4.25 us: 1.06x faster                                                            |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                                            |
| pickle_dict          | 28.3 us                                                | 32.0 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.95 ms: 1.56x faster                                                            |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.67 ms: 1.47x faster                                                            |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                            |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                            |
| genshi_xml      | 63.6 ms                                                | 46.7 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                                            |
| logging_silent          | 173 ns                                                 | 93.2 ns: 1.86x faster                                                            |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.79x faster                                                             |
| pyflate                 | 675 ms                                                 | 398 ms: 1.70x faster                                                             |
| richards                | 71.4 ms                                                | 42.1 ms: 1.69x faster                                                            |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                             |
| chaos                   | 104 ms                                                 | 63.4 ms: 1.64x faster                                                            |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                                             |
| scimark_monte_carlo     | 105 ms                                                 | 64.7 ms: 1.62x faster                                                            |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.61x faster                                                            |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.59x faster                                                             |
| hexiom                  | 9.42 ms                                                | 5.97 ms: 1.58x faster                                                            |
| python_startup          | 13.9 ms                                                | 8.95 ms: 1.56x faster                                                            |
| spectral_norm           | 148 ms                                                 | 95.9 ms: 1.54x faster                                                            |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                                             |
| float                   | 108 ms                                                 | 72.5 ms: 1.49x faster                                                            |
| mako                    | 14.3 ms                                                | 9.67 ms: 1.47x faster                                                            |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                            |
| deepcopy_memo           | 50.0 us                                                | 34.3 us: 1.46x faster                                                            |
| scimark_lu              | 158 ms                                                 | 109 ms: 1.46x faster                                                             |
| nbody                   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.43x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                            |
| unpack_sequence         | 59.5 ns                                                | 41.7 ns: 1.42x faster                                                            |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                                           |
| sqlglot_transpile       | 2.42 ms                                                | 1.72 ms: 1.41x faster                                                            |
| html5lib                | 85.8 ms                                                | 61.1 ms: 1.40x faster                                                            |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                            |
| logging_format          | 8.92 us                                                | 6.48 us: 1.38x faster                                                            |
| logging_simple          | 8.06 us                                                | 5.88 us: 1.37x faster                                                            |
| pprint_safe_repr        | 943 ms                                                 | 689 ms: 1.37x faster                                                             |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.01 ms: 1.37x faster                                                            |
| thrift                  | 1.03 ms                                                | 757 us: 1.36x faster                                                             |
| genshi_xml              | 63.6 ms                                                | 46.7 ms: 1.36x faster                                                            |
| chameleon               | 8.86 ms                                                | 6.51 ms: 1.36x faster                                                            |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                                           |
| tornado_http            | 128 ms                                                 | 94.4 ms: 1.36x faster                                                            |
| scimark_fft             | 414 ms                                                 | 305 ms: 1.36x faster                                                             |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                                            |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                           |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 639 ms: 1.34x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                            |
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                             |
| deepcopy                | 429 us                                                 | 329 us: 1.30x faster                                                             |
| fannkuch                | 477 ms                                                 | 368 ms: 1.29x faster                                                             |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                                            |
| nqueens                 | 99.3 ms                                                | 76.9 ms: 1.29x faster                                                            |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                            |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                           |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                                             |
| coroutines              | 31.7 ms                                                | 25.4 ms: 1.25x faster                                                            |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                                            |
| sympy_integrate         | 23.9 ms                                                | 20.0 ms: 1.20x faster                                                            |
| bench_thread_pool       | 943 us                                                 | 787 us: 1.20x faster                                                             |
| dulwich_log             | 75.5 ms                                                | 63.1 ms: 1.20x faster                                                            |
| sympy_str               | 324 ms                                                 | 272 ms: 1.19x faster                                                             |
| xml_etree_generate      | 93.3 ms                                                | 79.7 ms: 1.17x faster                                                            |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                                            |
| sympy_expand            | 537 ms                                                 | 459 ms: 1.17x faster                                                             |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                                           |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| sqlite_synth            | 2.90 us                                                | 2.60 us: 1.12x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                             |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                            |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                             |
| pickle_list             | 4.50 us                                                | 4.25 us: 1.06x faster                                                            |
| telco                   | 6.68 ms                                                | 6.38 ms: 1.05x faster                                                            |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                             |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                                            |
| async_generators        | 428 ms                                                 | 424 ms: 1.01x faster                                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                             |
| generators              | 75.8 ms                                                | 76.6 ms: 1.01x slower                                                            |
| regex_effbot            | 3.21 ms                                                | 3.36 ms: 1.05x slower                                                            |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                                            |
| pickle_dict             | 28.3 us                                                | 32.0 us: 1.13x slower                                                            |
| coverage                | 75.3 ms                                                | 96.5 ms: 1.28x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230206-3.12.0a4+-0c3dc7b/bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
