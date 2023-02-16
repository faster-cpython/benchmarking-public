
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.26x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 259 ms: 1.29x faster                                               |
| chameleon      | 9.17 ms                                                | 6.47 ms: 1.42x faster                                              |
| docutils       | 3.18 sec                                               | 2.61 sec: 1.21x faster                                             |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.41x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.2 ms: 1.50x faster                                              |
| float          | 109 ms                                                 | 74.9 ms: 1.45x faster                                              |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.28x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                              |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                               |
| regex_effbot   | 3.19 ms                                                | 3.47 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 299 us: 1.51x faster                                               |
| unpickle_pure_python | 302 us                                                 | 205 us: 1.47x faster                                               |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 54.9 ms: 1.36x faster                                              |
| xml_etree_generate   | 93.8 ms                                                | 78.8 ms: 1.19x faster                                              |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                              |
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                              |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                              |
| unpickle_list        | 4.92 us                                                | 4.88 us: 1.01x faster                                              |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.60 ms: 1.64x faster                                              |
| python_startup_no_site | 5.78 ms                                                | 6.13 ms: 1.06x slower                                              |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.85 ms: 1.49x faster                                              |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| django_template | 46.3 ms                                                | 34.5 ms: 1.34x faster                                              |
| genshi_xml      | 63.7 ms                                                | 47.8 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.42 ms: 2.13x faster                                              |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                               |
| logging_silent          | 176 ns                                                 | 98.6 ns: 1.79x faster                                              |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.78x faster                                               |
| richards                | 75.2 ms                                                | 44.4 ms: 1.69x faster                                              |
| pyflate                 | 676 ms                                                 | 409 ms: 1.65x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 66.1 ms: 1.64x faster                                              |
| python_startup          | 14.1 ms                                                | 8.60 ms: 1.64x faster                                              |
| go                      | 226 ms                                                 | 141 ms: 1.60x faster                                               |
| raytrace                | 467 ms                                                 | 301 ms: 1.55x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 75.9 ms: 1.54x faster                                              |
| chaos                   | 106 ms                                                 | 69.0 ms: 1.53x faster                                              |
| pickle_pure_python      | 452 us                                                 | 299 us: 1.51x faster                                               |
| nbody                   | 144 ms                                                 | 96.2 ms: 1.50x faster                                              |
| hexiom                  | 9.43 ms                                                | 6.31 ms: 1.49x faster                                              |
| spectral_norm           | 150 ms                                                 | 100 ms: 1.49x faster                                               |
| mako                    | 14.7 ms                                                | 9.85 ms: 1.49x faster                                              |
| unpickle_pure_python    | 302 us                                                 | 205 us: 1.47x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                               |
| float                   | 109 ms                                                 | 74.9 ms: 1.45x faster                                              |
| deepcopy_memo           | 51.7 us                                                | 35.8 us: 1.44x faster                                              |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.43x faster                                              |
| chameleon               | 9.17 ms                                                | 6.47 ms: 1.42x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                              |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.41x faster                                              |
| pprint_pformat          | 1.98 sec                                               | 1.43 sec: 1.39x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.38x faster                                              |
| thrift                  | 1.03 ms                                                | 753 us: 1.37x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 697 ms: 1.37x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.78 ms: 1.36x faster                                              |
| xml_etree_process       | 74.5 ms                                                | 54.9 ms: 1.36x faster                                              |
| logging_format          | 8.85 us                                                | 6.57 us: 1.35x faster                                              |
| logging_simple          | 8.10 us                                                | 6.01 us: 1.35x faster                                              |
| django_template         | 46.3 ms                                                | 34.5 ms: 1.34x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.07 ms: 1.34x faster                                              |
| scimark_fft             | 421 ms                                                 | 315 ms: 1.34x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                             |
| genshi_xml              | 63.7 ms                                                | 47.8 ms: 1.33x faster                                              |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                               |
| async_tree_none         | 711 ms                                                 | 534 ms: 1.33x faster                                               |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                             |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| 2to3                    | 335 ms                                                 | 259 ms: 1.29x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 667 ms: 1.28x faster                                               |
| nqueens                 | 100 ms                                                 | 78.9 ms: 1.27x faster                                              |
| deepcopy                | 438 us                                                 | 350 us: 1.25x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 53.0 ms: 1.23x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 109 ms: 1.23x faster                                               |
| coroutines              | 31.6 ms                                                | 26.0 ms: 1.22x faster                                              |
| docutils                | 3.18 sec                                               | 2.61 sec: 1.21x faster                                             |
| deepcopy_reduce         | 3.79 us                                                | 3.12 us: 1.21x faster                                              |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 78.8 ms: 1.19x faster                                              |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                              |
| bench_thread_pool       | 946 us                                                 | 801 us: 1.18x faster                                               |
| dulwich_log             | 75.8 ms                                                | 64.3 ms: 1.18x faster                                              |
| sympy_expand            | 534 ms                                                 | 470 ms: 1.13x faster                                               |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                              |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                              |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                              |
| json                    | 5.35 ms                                                | 4.74 ms: 1.13x faster                                              |
| sympy_str               | 325 ms                                                 | 291 ms: 1.12x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                              |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                               |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 22.1 ms: 1.09x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| mdp                     | 2.74 sec                                               | 2.55 sec: 1.08x faster                                             |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                              |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                              |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                               |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                              |
| unpickle_list           | 4.92 us                                                | 4.88 us: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                               |
| generators              | 76.4 ms                                                | 79.9 ms: 1.05x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.13 ms: 1.06x slower                                              |
| regex_effbot            | 3.19 ms                                                | 3.47 ms: 1.09x slower                                              |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                              |
| dask                    | 436 ms                                                 | 519 ms: 1.19x slower                                               |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                              |
| coverage                | 74.7 ms                                                | 101 ms: 1.35x slower                                               |
| Geometric mean          | (ref)                                                  | 1.26x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-1c97383/bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383.json: mypy
