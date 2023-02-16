
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 258 ms: 1.30x faster                                              |
| chameleon      | 9.17 ms                                                | 6.52 ms: 1.40x faster                                             |
| docutils       | 3.18 sec                                               | 2.60 sec: 1.22x faster                                            |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.6 ms: 1.51x faster                                             |
| float          | 109 ms                                                 | 73.5 ms: 1.48x faster                                             |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                             |
| regex_dna      | 214 ms                                                 | 219 ms: 1.03x slower                                              |
| regex_effbot   | 3.19 ms                                                | 3.60 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 295 us: 1.53x faster                                              |
| unpickle_pure_python | 302 us                                                 | 207 us: 1.45x faster                                              |
| json_dumps           | 13.4 ms                                                | 9.59 ms: 1.40x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 54.7 ms: 1.36x faster                                             |
| xml_etree_generate   | 93.8 ms                                                | 78.3 ms: 1.20x faster                                             |
| json_loads           | 28.7 us                                                | 24.5 us: 1.17x faster                                             |
| pickle_list          | 4.72 us                                                | 4.06 us: 1.16x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                             |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                             |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.59 ms: 1.64x faster                                             |
| python_startup_no_site | 5.78 ms                                                | 6.10 ms: 1.06x slower                                             |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.77 ms: 1.50x faster                                             |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                             |
| django_template | 46.3 ms                                                | 33.9 ms: 1.37x faster                                             |
| genshi_xml      | 63.7 ms                                                | 48.4 ms: 1.32x faster                                             |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.38 ms: 2.16x faster                                             |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                              |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                              |
| logging_silent          | 176 ns                                                 | 97.7 ns: 1.81x faster                                             |
| richards                | 75.2 ms                                                | 43.8 ms: 1.72x faster                                             |
| pyflate                 | 676 ms                                                 | 411 ms: 1.65x faster                                              |
| python_startup          | 14.1 ms                                                | 8.59 ms: 1.64x faster                                             |
| go                      | 226 ms                                                 | 139 ms: 1.62x faster                                              |
| scimark_monte_carlo     | 109 ms                                                 | 68.1 ms: 1.59x faster                                             |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.57x faster                                             |
| crypto_pyaes            | 117 ms                                                 | 74.7 ms: 1.56x faster                                             |
| raytrace                | 467 ms                                                 | 301 ms: 1.55x faster                                              |
| pickle_pure_python      | 452 us                                                 | 295 us: 1.53x faster                                              |
| spectral_norm           | 150 ms                                                 | 97.9 ms: 1.53x faster                                             |
| hexiom                  | 9.43 ms                                                | 6.25 ms: 1.51x faster                                             |
| nbody                   | 144 ms                                                 | 95.6 ms: 1.51x faster                                             |
| mako                    | 14.7 ms                                                | 9.77 ms: 1.50x faster                                             |
| float                   | 109 ms                                                 | 73.5 ms: 1.48x faster                                             |
| deepcopy_memo           | 51.7 us                                                | 35.2 us: 1.47x faster                                             |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                              |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                             |
| unpickle_pure_python    | 302 us                                                 | 207 us: 1.45x faster                                              |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                             |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                             |
| chameleon               | 9.17 ms                                                | 6.52 ms: 1.40x faster                                             |
| json_dumps              | 13.4 ms                                                | 9.59 ms: 1.40x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.40x faster                                             |
| pprint_pformat          | 1.98 sec                                               | 1.42 sec: 1.39x faster                                            |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.76 ms: 1.38x faster                                             |
| pprint_safe_repr        | 953 ms                                                 | 695 ms: 1.37x faster                                              |
| logging_simple          | 8.10 us                                                | 5.92 us: 1.37x faster                                             |
| django_template         | 46.3 ms                                                | 33.9 ms: 1.37x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 54.7 ms: 1.36x faster                                             |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                             |
| logging_format          | 8.85 us                                                | 6.59 us: 1.34x faster                                             |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                            |
| scimark_fft             | 421 ms                                                 | 316 ms: 1.33x faster                                              |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                            |
| genshi_xml              | 63.7 ms                                                | 48.4 ms: 1.32x faster                                             |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                              |
| 2to3                    | 335 ms                                                 | 258 ms: 1.30x faster                                              |
| fannkuch                | 488 ms                                                 | 380 ms: 1.28x faster                                              |
| async_tree_memoization  | 855 ms                                                 | 670 ms: 1.28x faster                                              |
| deepcopy                | 438 us                                                 | 345 us: 1.27x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 3.02 us: 1.25x faster                                             |
| nqueens                 | 100 ms                                                 | 79.9 ms: 1.25x faster                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 762 ms: 1.25x faster                                              |
| sqlglot_optimize        | 65.2 ms                                                | 53.0 ms: 1.23x faster                                             |
| docutils                | 3.18 sec                                               | 2.60 sec: 1.22x faster                                            |
| sqlglot_normalize       | 134 ms                                                 | 110 ms: 1.22x faster                                              |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 78.3 ms: 1.20x faster                                             |
| bench_thread_pool       | 946 us                                                 | 795 us: 1.19x faster                                              |
| dulwich_log             | 75.8 ms                                                | 64.1 ms: 1.18x faster                                             |
| coroutines              | 31.6 ms                                                | 26.8 ms: 1.18x faster                                             |
| json_loads              | 28.7 us                                                | 24.5 us: 1.17x faster                                             |
| pickle_list             | 4.72 us                                                | 4.06 us: 1.16x faster                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.43 ms: 1.16x faster                                             |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                             |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                             |
| sympy_expand            | 534 ms                                                 | 475 ms: 1.12x faster                                              |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                             |
| sympy_str               | 325 ms                                                 | 291 ms: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| mdp                     | 2.74 sec                                               | 2.50 sec: 1.10x faster                                            |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 22.1 ms: 1.09x faster                                             |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                              |
| telco                   | 6.73 ms                                                | 6.35 ms: 1.06x faster                                             |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                             |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                              |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                             |
| generators              | 76.4 ms                                                | 77.6 ms: 1.01x slower                                             |
| regex_dna               | 214 ms                                                 | 219 ms: 1.03x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.10 ms: 1.06x slower                                             |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                             |
| regex_effbot            | 3.19 ms                                                | 3.60 ms: 1.13x slower                                             |
| gc_traversal            | 3.53 ms                                                | 4.15 ms: 1.18x slower                                             |
| dask                    | 436 ms                                                 | 516 ms: 1.18x slower                                              |
| coverage                | 74.7 ms                                                | 99.1 ms: 1.33x slower                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: mypy
