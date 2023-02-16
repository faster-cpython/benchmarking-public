
# Results vs. 3.10.4

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.33x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                       |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.6 ms: 1.51x faster                                                       |
| float          | 109 ms                                                 | 73.8 ms: 1.48x faster                                                       |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                       |
| regex_dna      | 214 ms                                                 | 202 ms: 1.06x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.36 ms: 1.44x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 77.1 ms: 1.22x faster                                                       |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.22 us: 1.12x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| unpickle_list        | 4.92 us                                                | 4.94 us: 1.00x slower                                                       |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                       |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.46 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| mako            | 14.7 ms                                                | 9.85 ms: 1.49x faster                                                       |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 47.5 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                                       |
| logging_silent          | 176 ns                                                 | 90.0 ns: 1.96x faster                                                       |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 495 ms: 1.85x faster                                                        |
| richards                | 75.2 ms                                                | 41.9 ms: 1.79x faster                                                       |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                        |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                        |
| pyflate                 | 676 ms                                                 | 406 ms: 1.67x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 66.1 ms: 1.64x faster                                                       |
| chaos                   | 106 ms                                                 | 64.5 ms: 1.64x faster                                                       |
| hexiom                  | 9.43 ms                                                | 5.86 ms: 1.61x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                        |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.58x faster                                                       |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 74.0 ms: 1.58x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.52x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                        |
| nbody                   | 144 ms                                                 | 95.6 ms: 1.51x faster                                                       |
| mako                    | 14.7 ms                                                | 9.85 ms: 1.49x faster                                                       |
| float                   | 109 ms                                                 | 73.8 ms: 1.48x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.36 sec: 1.45x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.36 ms: 1.44x faster                                                       |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.41x faster                                                      |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 42.5 ns: 1.40x faster                                                       |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                        |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                        |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                                        |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                      |
| fannkuch                | 488 ms                                                 | 358 ms: 1.36x faster                                                        |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 630 ms: 1.36x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 992 us: 1.35x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.34x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 47.5 ms: 1.34x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                                       |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                                        |
| 2to3                    | 335 ms                                                 | 251 ms: 1.33x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                                       |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                        |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.9 ms: 1.27x faster                                                       |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 761 us: 1.24x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.1 ms: 1.22x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                       |
| async_generators        | 426 ms                                                 | 350 ms: 1.22x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 77.1 ms: 1.22x faster                                                       |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                        |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                       |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                                        |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                       |
| djangocms               | 36.9 us                                                | 32.0 us: 1.15x faster                                                       |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.22 us: 1.12x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                       |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                        |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                      |
| regex_dna               | 214 ms                                                 | 202 ms: 1.06x faster                                                        |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.05x faster                                                       |
| unpickle_list           | 4.92 us                                                | 4.94 us: 1.00x slower                                                       |
| generators              | 76.4 ms                                                | 76.9 ms: 1.01x slower                                                       |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                       |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.46 ms: 1.12x slower                                                       |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                                       |
| dask                    | 436 ms                                                 | 492 ms: 1.13x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                                       |
| coverage                | 74.7 ms                                                | 98.3 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230129-3.12.0a4+-23ae36b/bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b.json: mypy
