
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 61f1e67
- commit date: 2023-02-18
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                   |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.41x faster                                  |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.9 ms: 1.52x faster                                  |
| float          | 111 ms                                                 | 73.1 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 220 ms: 1.01x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.58 ms: 1.41x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.4 ms: 1.35x faster                                  |
| json_loads           | 28.8 us                                                | 23.7 us: 1.21x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.2 ms: 1.16x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| pickle_list          | 4.56 us                                                | 4.29 us: 1.06x faster                                  |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                  |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.06 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 32.5 us: 1.19x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.00 ms: 1.57x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.92 ms: 1.49x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| django_template | 45.9 ms                                                | 34.0 ms: 1.35x faster                                  |
| genshi_xml      | 63.3 ms                                                | 48.3 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.5 ms: 2.52x faster                                  |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                  |
| logging_silent          | 175 ns                                                 | 93.9 ns: 1.87x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                   |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                   |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                  |
| go                      | 229 ms                                                 | 133 ms: 1.73x faster                                   |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.4 ms: 1.63x faster                                  |
| raytrace                | 464 ms                                                 | 285 ms: 1.62x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.62x faster                                  |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.62x faster                                  |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                   |
| python_startup          | 14.2 ms                                                | 9.00 ms: 1.57x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.13 ms: 1.55x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.6 ms: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                   |
| nbody                   | 142 ms                                                 | 92.9 ms: 1.52x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.7 ns: 1.52x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                   |
| float                   | 111 ms                                                 | 73.1 ms: 1.51x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                  |
| mako                    | 14.8 ms                                                | 9.92 ms: 1.49x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.58 ms: 1.41x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                  |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.41x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 682 ms: 1.40x faster                                   |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| logging_simple          | 8.07 us                                                | 5.80 us: 1.39x faster                                  |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                  |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                   |
| logging_format          | 8.91 us                                                | 6.47 us: 1.38x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.98 ms: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                   |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 55.4 ms: 1.35x faster                                  |
| django_template         | 45.9 ms                                                | 34.0 ms: 1.35x faster                                  |
| fannkuch                | 486 ms                                                 | 360 ms: 1.35x faster                                   |
| thrift                  | 1.03 ms                                                | 766 us: 1.35x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                 |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                 |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                  |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 649 ms: 1.32x faster                                   |
| genshi_xml              | 63.3 ms                                                | 48.3 ms: 1.31x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 749 ms: 1.27x faster                                   |
| nqueens                 | 100 ms                                                 | 80.0 ms: 1.25x faster                                  |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 19.9 ms: 1.22x faster                                  |
| json_loads              | 28.8 us                                                | 23.7 us: 1.21x faster                                  |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                  |
| sympy_str               | 328 ms                                                 | 273 ms: 1.20x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                   |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                   |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                   |
| json                    | 5.42 ms                                                | 4.54 ms: 1.19x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                  |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 81.2 ms: 1.16x faster                                  |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                 |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                   |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                  |
| pickle_list             | 4.56 us                                                | 4.29 us: 1.06x faster                                  |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                  |
| async_generators        | 425 ms                                                 | 411 ms: 1.04x faster                                   |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                  |
| regex_dna               | 222 ms                                                 | 220 ms: 1.01x faster                                   |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| regex_effbot            | 3.23 ms                                                | 3.38 ms: 1.05x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.06 us: 1.05x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                  |
| dask                    | 423 ms                                                 | 501 ms: 1.19x slower                                   |
| pickle_dict             | 27.3 us                                                | 32.5 us: 1.19x slower                                  |
| coverage                | 72.8 ms                                                | 96.3 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
