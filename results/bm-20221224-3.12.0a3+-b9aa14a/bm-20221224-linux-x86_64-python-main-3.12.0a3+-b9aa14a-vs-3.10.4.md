
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9aa14a
- commit date: 2022-12-24
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.17 ms                                                | 6.38 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 72.1 ms: 1.51x faster                                  |
| nbody          | 144 ms                                                 | 96.5 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.40 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.9 ms: 1.24x faster                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.25 us: 1.11x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| pickle               | 10.2 us                                                | 10.3 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 32.4 us: 1.18x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.49 ms: 1.66x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.08 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.59 ms: 1.53x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                  |
| django_template | 46.3 ms                                                | 33.0 ms: 1.41x faster                                  |
| genshi_xml      | 63.7 ms                                                | 49.0 ms: 1.30x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.27 ms: 2.23x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| logging_silent          | 176 ns                                                 | 94.8 ns: 1.86x faster                                  |
| richards                | 75.2 ms                                                | 41.8 ms: 1.80x faster                                  |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                   |
| python_startup          | 14.1 ms                                                | 8.49 ms: 1.66x faster                                  |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.6 ms: 1.65x faster                                  |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                   |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.2 ms: 1.55x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.09 ms: 1.55x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 33.4 us: 1.55x faster                                  |
| mako                    | 14.7 ms                                                | 9.59 ms: 1.53x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                   |
| chaos                   | 106 ms                                                 | 69.6 ms: 1.52x faster                                  |
| float                   | 109 ms                                                 | 72.1 ms: 1.51x faster                                  |
| nbody                   | 144 ms                                                 | 96.5 ms: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                   |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                 |
| chameleon               | 9.17 ms                                                | 6.38 ms: 1.44x faster                                  |
| logging_simple          | 8.10 us                                                | 5.67 us: 1.43x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                  |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 671 ms: 1.42x faster                                   |
| logging_format          | 8.85 us                                                | 6.29 us: 1.41x faster                                  |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.41x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                 |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 622 ms: 1.37x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| scimark_fft             | 421 ms                                                 | 316 ms: 1.33x faster                                   |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                   |
| fannkuch                | 488 ms                                                 | 375 ms: 1.30x faster                                   |
| genshi_xml              | 63.7 ms                                                | 49.0 ms: 1.30x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.25 ms: 1.28x faster                                  |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                   |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.27x faster                                  |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 759 ms: 1.25x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 75.9 ms: 1.24x faster                                  |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                  |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                   |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                   |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                   |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                  |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                   |
| json                    | 5.35 ms                                                | 4.74 ms: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| pickle_list             | 4.72 us                                                | 4.25 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                   |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| telco                   | 6.73 ms                                                | 6.25 ms: 1.08x faster                                  |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                   |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| generators              | 76.4 ms                                                | 77.6 ms: 1.02x slower                                  |
| pickle                  | 10.2 us                                                | 10.3 us: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.08 ms: 1.05x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.40 ms: 1.06x slower                                  |
| pickle_dict             | 27.6 us                                                | 32.4 us: 1.18x slower                                  |
| coverage                | 74.7 ms                                                | 98.1 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221224-3.12.0a3+-b9aa14a/bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a.json: mypy
