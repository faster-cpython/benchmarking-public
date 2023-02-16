
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
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.29 ms: 1.46x faster                                                        |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                 | 71.3 ms: 1.53x faster                                                        |
| nbody          | 144 ms                                                 | 95.2 ms: 1.51x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| regex_dna      | 214 ms                                                 | 215 ms: 1.01x slower                                                         |
| regex_effbot   | 3.19 ms                                                | 3.69 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 76.2 ms: 1.23x faster                                                        |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.23 us: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                        |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                                        |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.52 ms: 1.65x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.09 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.79 ms: 1.50x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.50x faster                                                        |
| django_template | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                        |
| logging_silent          | 176 ns                                                 | 92.7 ns: 1.90x faster                                                        |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                         |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.83x faster                                                         |
| richards                | 75.2 ms                                                | 42.9 ms: 1.75x faster                                                        |
| pyflate                 | 676 ms                                                 | 395 ms: 1.71x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 64.4 ms: 1.68x faster                                                        |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                         |
| python_startup          | 14.1 ms                                                | 8.52 ms: 1.65x faster                                                        |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                         |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                         |
| spectral_norm           | 150 ms                                                 | 95.3 ms: 1.57x faster                                                        |
| chaos                   | 106 ms                                                 | 67.8 ms: 1.56x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 33.4 us: 1.55x faster                                                        |
| hexiom                  | 9.43 ms                                                | 6.12 ms: 1.54x faster                                                        |
| float                   | 109 ms                                                 | 71.3 ms: 1.53x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                         |
| crypto_pyaes            | 117 ms                                                 | 76.9 ms: 1.52x faster                                                        |
| nbody                   | 144 ms                                                 | 95.2 ms: 1.51x faster                                                        |
| mako                    | 14.7 ms                                                | 9.79 ms: 1.50x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.50x faster                                                        |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                                         |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.29 ms: 1.46x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.44x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                        |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                                         |
| unpack_sequence         | 59.4 ns                                                | 41.8 ns: 1.42x faster                                                        |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                        |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                                        |
| thrift                  | 1.03 ms                                                | 752 us: 1.37x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                       |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                         |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.35x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 635 ms: 1.35x faster                                                         |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.34x faster                                                         |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                         |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                                         |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                       |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.89 us: 1.31x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.22 ms: 1.29x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 748 ms: 1.27x faster                                                         |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.26x faster                                                         |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.3 ms: 1.25x faster                                                        |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 76.2 ms: 1.23x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.2 ms: 1.22x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                                         |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                         |
| sympy_integrate         | 24.0 ms                                                | 19.9 ms: 1.21x faster                                                        |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                         |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                                        |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                         |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.15x faster                                                        |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.23 us: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| mdp                     | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| telco                   | 6.73 ms                                                | 6.25 ms: 1.08x faster                                                        |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                        |
| generators              | 76.4 ms                                                | 76.6 ms: 1.00x slower                                                        |
| regex_dna               | 214 ms                                                 | 215 ms: 1.01x slower                                                         |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| gc_traversal            | 3.53 ms                                                | 3.63 ms: 1.03x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.09 ms: 1.06x slower                                                        |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                                        |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                                         |
| regex_effbot            | 3.19 ms                                                | 3.69 ms: 1.16x slower                                                        |
| coverage                | 74.7 ms                                                | 97.5 ms: 1.30x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-6ec191a/bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a.json: mypy
