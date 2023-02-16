
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.17 ms                                                | 6.21 ms: 1.48x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 59.9 ms: 1.43x faster                                               |
| tornado_http   | 128 ms                                                 | 93.6 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 73.1 ms: 1.49x faster                                               |
| nbody          | 144 ms                                                 | 96.7 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                               |
| regex_dna      | 214 ms                                                 | 217 ms: 1.01x slower                                                |
| regex_effbot   | 3.19 ms                                                | 3.77 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.41 ms: 1.43x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.39x faster                                               |
| json_loads           | 28.7 us                                                | 23.4 us: 1.23x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.5 ms: 1.21x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 145 ms: 1.12x faster                                                |
| pickle_list          | 4.72 us                                                | 4.22 us: 1.12x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                               |
| unpickle_list        | 4.92 us                                                | 5.15 us: 1.05x slower                                               |
| pickle_dict          | 27.6 us                                                | 31.8 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.50 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.47 ms: 1.55x faster                                               |
| django_template | 46.3 ms                                                | 32.1 ms: 1.44x faster                                               |
| genshi_text     | 30.6 ms                                                | 21.3 ms: 1.44x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.5 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.18 ms: 2.29x faster                                               |
| logging_silent          | 176 ns                                                 | 92.8 ns: 1.90x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 492 ms: 1.86x faster                                                |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 41.9 ms: 1.80x faster                                               |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                                |
| chaos                   | 106 ms                                                 | 63.7 ms: 1.66x faster                                               |
| pyflate                 | 676 ms                                                 | 410 ms: 1.65x faster                                                |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 67.0 ms: 1.62x faster                                               |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                |
| hexiom                  | 9.43 ms                                                | 5.93 ms: 1.59x faster                                               |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                               |
| spectral_norm           | 150 ms                                                 | 96.6 ms: 1.55x faster                                               |
| mako                    | 14.7 ms                                                | 9.47 ms: 1.55x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 76.1 ms: 1.53x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                |
| float                   | 109 ms                                                 | 73.1 ms: 1.49x faster                                               |
| nbody                   | 144 ms                                                 | 96.7 ms: 1.49x faster                                               |
| chameleon               | 9.17 ms                                                | 6.21 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                               |
| django_template         | 46.3 ms                                                | 32.1 ms: 1.44x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                               |
| genshi_text             | 30.6 ms                                                | 21.3 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 59.9 ms: 1.43x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.41 ms: 1.43x faster                                               |
| logging_simple          | 8.10 us                                                | 5.67 us: 1.43x faster                                               |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 42.5 ns: 1.40x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.39x faster                                               |
| scimark_fft             | 421 ms                                                 | 304 ms: 1.38x faster                                                |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| tornado_http            | 128 ms                                                 | 93.6 ms: 1.37x faster                                               |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                               |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                              |
| deepcopy                | 438 us                                                 | 326 us: 1.34x faster                                                |
| genshi_xml              | 63.7 ms                                                | 47.5 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| fannkuch                | 488 ms                                                 | 368 ms: 1.33x faster                                                |
| coroutines              | 31.6 ms                                                | 24.1 ms: 1.31x faster                                               |
| nqueens                 | 100 ms                                                 | 77.2 ms: 1.30x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 660 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                                |
| json_loads              | 28.7 us                                                | 23.4 us: 1.23x faster                                               |
| bench_thread_pool       | 946 us                                                 | 777 us: 1.22x faster                                                |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.22x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.4 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 77.5 ms: 1.21x faster                                               |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                                |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                |
| json                    | 5.35 ms                                                | 4.59 ms: 1.17x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.54 us: 1.15x faster                                               |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 145 ms: 1.12x faster                                                |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                               |
| pickle_list             | 4.72 us                                                | 4.22 us: 1.12x faster                                               |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                              |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                               |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                               |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| regex_dna               | 214 ms                                                 | 217 ms: 1.01x slower                                                |
| generators              | 76.4 ms                                                | 77.7 ms: 1.02x slower                                               |
| unpickle_list           | 4.92 us                                                | 5.15 us: 1.05x slower                                               |
| gc_traversal            | 3.53 ms                                                | 3.93 ms: 1.11x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.50 ms: 1.13x slower                                               |
| dask                    | 436 ms                                                 | 494 ms: 1.13x slower                                                |
| pickle_dict             | 27.6 us                                                | 31.8 us: 1.15x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.77 ms: 1.18x slower                                               |
| coverage                | 74.7 ms                                                | 94.8 ms: 1.27x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-5609e30/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30.json: mypy
