
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| chameleon      | 9.06 ms                                                | 6.93 ms: 1.31x faster                                  |
| docutils       | 3.17 sec                                               | 2.70 sec: 1.17x faster                                 |
| html5lib       | 85.9 ms                                                | 65.0 ms: 1.32x faster                                  |
| tornado_http   | 127 ms                                                 | 104 ms: 1.22x faster                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.4 ms: 1.60x faster                                  |
| float          | 111 ms                                                 | 80.4 ms: 1.37x faster                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.26 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.47x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 58.6 ms: 1.28x faster                                  |
| json_loads           | 28.8 us                                                | 24.8 us: 1.16x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 83.2 ms: 1.13x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                   |
| pickle_list          | 4.56 us                                                | 4.39 us: 1.04x faster                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.24 us: 1.09x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.05 ms: 1.56x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.65 ms: 1.14x slower                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.5 ms: 1.40x faster                                  |
| genshi_text     | 30.3 ms                                                | 22.7 ms: 1.34x faster                                  |
| django_template | 45.9 ms                                                | 34.7 ms: 1.32x faster                                  |
| genshi_xml      | 63.3 ms                                                | 50.7 ms: 1.25x faster                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.2 ms: 2.46x faster                                  |
| deltablue               | 7.42 ms                                                | 3.64 ms: 2.04x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 511 ms: 1.81x faster                                   |
| logging_silent          | 175 ns                                                 | 101 ns: 1.73x faster                                   |
| richards                | 74.9 ms                                                | 44.0 ms: 1.70x faster                                  |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                   |
| nbody                   | 142 ms                                                 | 88.4 ms: 1.60x faster                                  |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.59x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.31 ms: 1.57x faster                                  |
| python_startup          | 14.2 ms                                                | 9.05 ms: 1.56x faster                                  |
| raytrace                | 464 ms                                                 | 300 ms: 1.55x faster                                   |
| chaos                   | 106 ms                                                 | 69.3 ms: 1.53x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.34 ms: 1.50x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 78.9 ms: 1.50x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                  |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 73.3 ms: 1.48x faster                                  |
| pyflate                 | 673 ms                                                 | 459 ms: 1.47x faster                                   |
| pickle_pure_python      | 455 us                                                 | 311 us: 1.47x faster                                   |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                   |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.42x faster                                  |
| mako                    | 14.8 ms                                                | 10.5 ms: 1.40x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.75 ms: 1.39x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 38.0 us: 1.38x faster                                  |
| float                   | 111 ms                                                 | 80.4 ms: 1.37x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 219 us: 1.37x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 47.4 ns: 1.37x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.48 sec: 1.34x faster                                 |
| genshi_text             | 30.3 ms                                                | 22.7 ms: 1.34x faster                                  |
| django_template         | 45.9 ms                                                | 34.7 ms: 1.32x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                   |
| html5lib                | 85.9 ms                                                | 65.0 ms: 1.32x faster                                  |
| logging_simple          | 8.07 us                                                | 6.17 us: 1.31x faster                                  |
| chameleon               | 9.06 ms                                                | 6.93 ms: 1.31x faster                                  |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                 |
| thrift                  | 1.03 ms                                                | 796 us: 1.30x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 737 ms: 1.30x faster                                   |
| logging_format          | 8.91 us                                                | 6.91 us: 1.29x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 742 ms: 1.28x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 58.6 ms: 1.28x faster                                  |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                   |
| 2to3                    | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| genshi_xml              | 63.3 ms                                                | 50.7 ms: 1.25x faster                                  |
| nqueens                 | 100 ms                                                 | 81.2 ms: 1.23x faster                                  |
| regex_compile           | 177 ms                                                 | 144 ms: 1.23x faster                                   |
| deepcopy                | 442 us                                                 | 360 us: 1.23x faster                                   |
| tornado_http            | 127 ms                                                 | 104 ms: 1.22x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.22x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.18 us: 1.20x faster                                  |
| scimark_fft             | 424 ms                                                 | 353 ms: 1.20x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 54.5 ms: 1.20x faster                                  |
| mypy2                   | 428 ms                                                 | 360 ms: 1.19x faster                                   |
| docutils                | 3.17 sec                                               | 2.70 sec: 1.17x faster                                 |
| json_loads              | 28.8 us                                                | 24.8 us: 1.16x faster                                  |
| comprehensions          | 26.8 us                                                | 23.3 us: 1.15x faster                                  |
| json                    | 5.42 ms                                                | 4.75 ms: 1.14x faster                                  |
| bench_thread_pool       | 947 us                                                 | 836 us: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 83.2 ms: 1.13x faster                                  |
| pylint                  | 525 ms                                                 | 466 ms: 1.13x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.13x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.86 ms: 1.12x faster                                  |
| dulwich_log             | 75.9 ms                                                | 67.8 ms: 1.12x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 21.9 ms: 1.11x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.2 ms: 1.10x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.66 us: 1.10x faster                                  |
| sympy_expand            | 545 ms                                                 | 496 ms: 1.10x faster                                   |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.07x faster                                   |
| djangocms               | 35.9 us                                                | 33.6 us: 1.07x faster                                  |
| sympy_str               | 328 ms                                                 | 311 ms: 1.06x faster                                   |
| pickle_list             | 4.56 us                                                | 4.39 us: 1.04x faster                                  |
| meteor_contest          | 115 ms                                                 | 111 ms: 1.03x faster                                   |
| sympy_sum               | 185 ms                                                 | 181 ms: 1.02x faster                                   |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| regex_effbot            | 3.23 ms                                                | 3.26 ms: 1.01x slower                                  |
| gc_traversal            | 3.84 ms                                                | 3.93 ms: 1.02x slower                                  |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| telco                   | 6.54 ms                                                | 6.83 ms: 1.04x slower                                  |
| async_generators        | 425 ms                                                 | 445 ms: 1.05x slower                                   |
| unpickle                | 14.1 us                                                | 14.9 us: 1.05x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.24 us: 1.09x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.65 ms: 1.14x slower                                  |
| dask                    | 423 ms                                                 | 539 ms: 1.28x slower                                   |
| coverage                | 72.8 ms                                                | 101 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.24x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x
