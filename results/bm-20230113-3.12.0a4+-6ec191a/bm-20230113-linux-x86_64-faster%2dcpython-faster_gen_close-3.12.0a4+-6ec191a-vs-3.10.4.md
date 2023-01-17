
# Results vs. 3.10.4

- fork: faster-cpython
- ref: faster_gen_close
- machine: linux-x86_64
- commit hash: 6ec191a
- commit date: 2023-01-13
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 250 ms: 1.33x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.29 ms: 1.41x faster                                                        |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| html5lib       | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.3 ms: 1.51x faster                                                        |
| nbody          | 136 ms                                                 | 95.2 ms: 1.43x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.34x faster                                                         |
| regex_dna      | 214 ms                                                 | 215 ms: 1.01x slower                                                         |
| regex_effbot   | 3.21 ms                                                | 3.69 ms: 1.15x slower                                                        |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.43x faster                                                        |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                                        |
| pickle_dict          | 28.3 us                                                | 31.2 us: 1.10x slower                                                        |
| pickle_list          | 4.50 us                                                | 4.23 us: 1.06x faster                                                        |
| pickle_pure_python   | 453 us                                                 | 284 us: 1.60x faster                                                         |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                        |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                         |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                         |
| xml_etree_generate   | 93.3 ms                                                | 76.2 ms: 1.22x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.52 ms: 1.63x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.09 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.7 ms: 1.41x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.50x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                        |
| mako            | 14.3 ms                                                | 9.79 ms: 1.46x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 250 ms: 1.33x faster                                                         |
| async_generators        | 428 ms                                                 | 352 ms: 1.22x faster                                                         |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 748 ms: 1.27x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.34x faster                                                         |
| chameleon               | 8.86 ms                                                | 6.29 ms: 1.41x faster                                                        |
| chaos                   | 104 ms                                                 | 67.8 ms: 1.53x faster                                                        |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                                         |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                                        |
| coverage                | 75.3 ms                                                | 97.5 ms: 1.29x slower                                                        |
| crypto_pyaes            | 118 ms                                                 | 76.9 ms: 1.53x faster                                                        |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                                         |
| deepcopy_reduce         | 3.75 us                                                | 2.89 us: 1.30x faster                                                        |
| deepcopy_memo           | 50.0 us                                                | 33.4 us: 1.50x faster                                                        |
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                                        |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.41x faster                                                        |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| dulwich_log             | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                        |
| fannkuch                | 477 ms                                                 | 371 ms: 1.29x faster                                                         |
| float                   | 108 ms                                                 | 71.3 ms: 1.51x faster                                                        |
| generators              | 75.8 ms                                                | 76.6 ms: 1.01x slower                                                        |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.50x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                        |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                         |
| hexiom                  | 9.42 ms                                                | 6.12 ms: 1.54x faster                                                        |
| html5lib                | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                        |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.43x faster                                                        |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                                        |
| logging_format          | 8.92 us                                                | 6.34 us: 1.41x faster                                                        |
| logging_silent          | 173 ns                                                 | 92.7 ns: 1.87x faster                                                        |
| logging_simple          | 8.06 us                                                | 5.74 us: 1.40x faster                                                        |
| mako                    | 14.3 ms                                                | 9.79 ms: 1.46x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.52 sec: 1.12x faster                                                       |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                         |
| mypy                    | 1.01 sec                                               | 804 ms: 1.26x faster                                                         |
| nbody                   | 136 ms                                                 | 95.2 ms: 1.43x faster                                                        |
| nqueens                 | 99.3 ms                                                | 80.8 ms: 1.23x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                        |
| pickle_dict             | 28.3 us                                                | 31.2 us: 1.10x slower                                                        |
| pickle_list             | 4.50 us                                                | 4.23 us: 1.06x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.60x faster                                                         |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                                         |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                       |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                       |
| pyflate                 | 675 ms                                                 | 395 ms: 1.71x faster                                                         |
| python_startup          | 13.9 ms                                                | 8.52 ms: 1.63x faster                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.09 ms: 1.06x slower                                                        |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                                         |
| regex_compile           | 174 ms                                                 | 130 ms: 1.34x faster                                                         |
| regex_dna               | 214 ms                                                 | 215 ms: 1.01x slower                                                         |
| regex_effbot            | 3.21 ms                                                | 3.69 ms: 1.15x slower                                                        |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                        |
| richards                | 71.4 ms                                                | 42.9 ms: 1.66x faster                                                        |
| scimark_fft             | 414 ms                                                 | 313 ms: 1.32x faster                                                         |
| scimark_lu              | 158 ms                                                 | 109 ms: 1.45x faster                                                         |
| scimark_monte_carlo     | 105 ms                                                 | 64.4 ms: 1.63x faster                                                        |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                         |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.22 ms: 1.30x faster                                                        |
| spectral_norm           | 148 ms                                                 | 95.3 ms: 1.55x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                        |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.43x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                         |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                        |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.18x faster                                                         |
| sympy_integrate         | 23.9 ms                                                | 19.9 ms: 1.21x faster                                                        |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                         |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                                         |
| telco                   | 6.68 ms                                                | 6.25 ms: 1.07x faster                                                        |
| thrift                  | 1.03 ms                                                | 752 us: 1.37x faster                                                         |
| unpack_sequence         | 59.5 ns                                                | 41.8 ns: 1.42x faster                                                        |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                        |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                         |
| xml_etree_generate      | 93.3 ms                                                | 76.2 ms: 1.22x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (3): bench_mp_pool, pickle, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-6ec191a/bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
