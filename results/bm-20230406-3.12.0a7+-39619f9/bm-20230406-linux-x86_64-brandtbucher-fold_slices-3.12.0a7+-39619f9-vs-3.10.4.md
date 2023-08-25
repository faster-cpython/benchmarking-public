
# Results vs. 3.10.4

- fork: brandtbucher
- ref: fold_slices
- machine: linux-x86_64
- commit hash: 39619f9
- commit date: 2023-04-06
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.35x faster                                                |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                               |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                               |
| tornado_http   | 127 ms                                                 | 90.9 ms: 1.40x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.6 ms: 1.63x faster                                               |
| float          | 111 ms                                                 | 73.6 ms: 1.50x faster                                               |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| regex_dna      | 222 ms                                                 | 204 ms: 1.08x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                                |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.53 ms: 1.42x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 56.2 ms: 1.33x faster                                               |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_list          | 4.56 us                                                | 4.35 us: 1.05x faster                                               |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                               |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                               |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.20x slower                                               |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.84 ms: 1.60x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                               |
| django_template | 45.9 ms                                                | 33.4 ms: 1.37x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.6 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.2 ms: 2.63x faster                                               |
| deltablue               | 7.42 ms                                                | 3.30 ms: 2.24x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                |
| logging_silent          | 175 ns                                                 | 97.7 ns: 1.79x faster                                               |
| richards                | 74.9 ms                                                | 42.5 ms: 1.76x faster                                               |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                                |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                |
| sqlglot_parse           | 2.06 ms                                                | 1.23 ms: 1.68x faster                                               |
| nbody                   | 142 ms                                                 | 86.6 ms: 1.63x faster                                               |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                                |
| sqlglot_transpile       | 2.45 ms                                                | 1.50 ms: 1.63x faster                                               |
| pyflate                 | 673 ms                                                 | 414 ms: 1.63x faster                                                |
| chaos                   | 106 ms                                                 | 65.9 ms: 1.61x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 73.5 ms: 1.61x faster                                               |
| python_startup          | 14.2 ms                                                | 8.84 ms: 1.60x faster                                               |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 68.3 ms: 1.58x faster                                               |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                                |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                               |
| float                   | 111 ms                                                 | 73.6 ms: 1.50x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 43.9 ns: 1.48x faster                                               |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                                |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.46x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.53 ms: 1.42x faster                                               |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                               |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                               |
| tornado_http            | 127 ms                                                 | 90.9 ms: 1.40x faster                                               |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                               |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                              |
| async_tree_none         | 717 ms                                                 | 515 ms: 1.39x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 690 ms: 1.38x faster                                                |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                               |
| django_template         | 45.9 ms                                                | 33.4 ms: 1.37x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 624 ms: 1.37x faster                                                |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                                |
| deepcopy                | 442 us                                                 | 326 us: 1.36x faster                                                |
| 2to3                    | 336 ms                                                 | 250 ms: 1.35x faster                                                |
| coroutines              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                               |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 56.2 ms: 1.33x faster                                               |
| genshi_xml              | 63.3 ms                                                | 47.6 ms: 1.33x faster                                               |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| async_tree_cpu_io_mixed | 951 ms                                                 | 736 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                               |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                               |
| fannkuch                | 486 ms                                                 | 380 ms: 1.28x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.31 ms: 1.27x faster                                               |
| comprehensions          | 26.8 us                                                | 21.4 us: 1.25x faster                                               |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                              |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.24x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                               |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                               |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                               |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                               |
| sympy_expand            | 545 ms                                                 | 467 ms: 1.17x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 80.9 ms: 1.16x faster                                               |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                                |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.13x faster                                              |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                               |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.51 ms: 1.10x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                |
| regex_dna               | 222 ms                                                 | 204 ms: 1.08x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_list             | 4.56 us                                                | 4.35 us: 1.05x faster                                               |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                               |
| async_generators        | 425 ms                                                 | 408 ms: 1.04x faster                                                |
| telco                   | 6.54 ms                                                | 6.32 ms: 1.04x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| unpickle_list           | 4.82 us                                                | 4.92 us: 1.02x slower                                               |
| pickle                  | 10.3 us                                                | 10.9 us: 1.06x slower                                               |
| gc_traversal            | 3.84 ms                                                | 4.10 ms: 1.07x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                               |
| pickle_dict             | 27.3 us                                                | 32.6 us: 1.20x slower                                               |
| dask                    | 423 ms                                                 | 507 ms: 1.20x slower                                                |
| coverage                | 72.8 ms                                                | 96.7 ms: 1.33x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
