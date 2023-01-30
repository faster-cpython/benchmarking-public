
# Results vs. 3.10.4

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                             |
| chameleon      | 8.86 ms                                                | 6.37 ms: 1.39x faster                                                            |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                           |
| html5lib       | 85.8 ms                                                | 60.2 ms: 1.43x faster                                                            |
| tornado_http   | 128 ms                                                 | 93.4 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.2 ms: 1.49x faster                                                            |
| nbody          | 136 ms                                                 | 93.7 ms: 1.45x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.33x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                             |
| regex_effbot   | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                                             |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                            |
| xml_etree_generate   | 93.3 ms                                                | 77.5 ms: 1.20x faster                                                            |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                            |
| pickle_list          | 4.50 us                                                | 4.10 us: 1.10x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                             |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                 | 105 ms: 1.05x faster                                                             |
| pickle_dict          | 28.3 us                                                | 30.7 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.57 ms: 1.63x faster                                                            |
| python_startup_no_site | 5.76 ms                                                | 6.13 ms: 1.06x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                            |
| mako            | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                            |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                            |
| genshi_xml      | 63.6 ms                                                | 46.5 ms: 1.37x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.19 ms: 2.32x faster                                                            |
| logging_silent          | 173 ns                                                 | 91.5 ns: 1.89x faster                                                            |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                             |
| pyflate                 | 675 ms                                                 | 394 ms: 1.72x faster                                                             |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                             |
| richards                | 71.4 ms                                                | 42.3 ms: 1.69x faster                                                            |
| scimark_monte_carlo     | 105 ms                                                 | 64.3 ms: 1.63x faster                                                            |
| python_startup          | 13.9 ms                                                | 8.57 ms: 1.63x faster                                                            |
| raytrace                | 461 ms                                                 | 287 ms: 1.61x faster                                                             |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                                             |
| hexiom                  | 9.42 ms                                                | 5.95 ms: 1.58x faster                                                            |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.58x faster                                                            |
| chaos                   | 104 ms                                                 | 66.9 ms: 1.56x faster                                                            |
| spectral_norm           | 148 ms                                                 | 97.6 ms: 1.52x faster                                                            |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                             |
| deepcopy_memo           | 50.0 us                                                | 33.5 us: 1.49x faster                                                            |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                            |
| float                   | 108 ms                                                 | 72.2 ms: 1.49x faster                                                            |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                                             |
| mako                    | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                            |
| nbody                   | 136 ms                                                 | 93.7 ms: 1.45x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                            |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                           |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                            |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                            |
| html5lib                | 85.8 ms                                                | 60.2 ms: 1.43x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.42x faster                                                            |
| pprint_safe_repr        | 943 ms                                                 | 666 ms: 1.42x faster                                                             |
| logging_format          | 8.92 us                                                | 6.31 us: 1.41x faster                                                            |
| logging_simple          | 8.06 us                                                | 5.71 us: 1.41x faster                                                            |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.39x faster                                                           |
| chameleon               | 8.86 ms                                                | 6.37 ms: 1.39x faster                                                            |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                            |
| thrift                  | 1.03 ms                                                | 746 us: 1.38x faster                                                             |
| unpack_sequence         | 59.5 ns                                                | 43.0 ns: 1.38x faster                                                            |
| tornado_http            | 128 ms                                                 | 93.4 ms: 1.37x faster                                                            |
| genshi_xml              | 63.6 ms                                                | 46.5 ms: 1.37x faster                                                            |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.01 ms: 1.37x faster                                                            |
| async_tree_none         | 713 ms                                                 | 523 ms: 1.36x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                           |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                            |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                            |
| regex_compile           | 174 ms                                                 | 130 ms: 1.33x faster                                                             |
| scimark_fft             | 414 ms                                                 | 312 ms: 1.33x faster                                                             |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                             |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                                             |
| deepcopy_reduce         | 3.75 us                                                | 2.89 us: 1.30x faster                                                            |
| deepcopy                | 429 us                                                 | 332 us: 1.29x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                             |
| coroutines              | 31.7 ms                                                | 24.7 ms: 1.28x faster                                                            |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                                             |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                           |
| mypy                    | 1.01 sec                                               | 810 ms: 1.25x faster                                                             |
| nqueens                 | 99.3 ms                                                | 79.4 ms: 1.25x faster                                                            |
| dulwich_log             | 75.5 ms                                                | 61.6 ms: 1.22x faster                                                            |
| bench_thread_pool       | 943 us                                                 | 778 us: 1.21x faster                                                             |
| xml_etree_generate      | 93.3 ms                                                | 77.5 ms: 1.20x faster                                                            |
| async_generators        | 428 ms                                                 | 355 ms: 1.20x faster                                                             |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                            |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                            |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.18x faster                                                             |
| sympy_str               | 324 ms                                                 | 281 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                           |
| json                    | 5.35 ms                                                | 4.72 ms: 1.13x faster                                                            |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                             |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                             |
| pickle_list             | 4.50 us                                                | 4.10 us: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                             |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                            |
| telco                   | 6.68 ms                                                | 6.24 ms: 1.07x faster                                                            |
| xml_etree_iterparse     | 110 ms                                                 | 105 ms: 1.05x faster                                                             |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                             |
| generators              | 75.8 ms                                                | 77.2 ms: 1.02x slower                                                            |
| python_startup_no_site  | 5.76 ms                                                | 6.13 ms: 1.06x slower                                                            |
| pickle_dict             | 28.3 us                                                | 30.7 us: 1.08x slower                                                            |
| regex_effbot            | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                            |
| coverage                | 75.3 ms                                                | 99.6 ms: 1.32x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                     |

Benchmark hidden because not significant (3): unpickle_list, pickle, bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230113-3.12.0a4+-df06ef8/bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
