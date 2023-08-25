
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.43x faster                                                        |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.8 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                                        |
| float          | 111 ms                                                 | 73.0 ms: 1.51x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| regex_dna      | 222 ms                                                 | 218 ms: 1.02x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.33 ms: 1.45x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 55.3 ms: 1.36x faster                                                        |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.5 ms: 1.17x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.13 us: 1.10x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| unpickle             | 14.1 us                                                | 13.7 us: 1.04x faster                                                        |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.86 ms: 1.60x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.42 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.90 ms: 1.49x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                        |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                                        |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                         |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                                         |
| logging_silent          | 175 ns                                                 | 95.9 ns: 1.83x faster                                                        |
| richards                | 74.9 ms                                                | 42.8 ms: 1.75x faster                                                        |
| go                      | 229 ms                                                 | 134 ms: 1.72x faster                                                         |
| pyflate                 | 673 ms                                                 | 406 ms: 1.66x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 66.1 ms: 1.64x faster                                                        |
| raytrace                | 464 ms                                                 | 286 ms: 1.62x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 73.6 ms: 1.61x faster                                                        |
| spectral_norm           | 150 ms                                                 | 93.4 ms: 1.61x faster                                                        |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.60x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.86 ms: 1.60x faster                                                        |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 294 us: 1.55x faster                                                         |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                        |
| float                   | 111 ms                                                 | 73.0 ms: 1.51x faster                                                        |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                         |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                         |
| mako                    | 14.8 ms                                                | 9.90 ms: 1.49x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 44.2 ns: 1.46x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.33 ms: 1.45x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.43x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                        |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                         |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.37x faster                                                         |
| logging_format          | 8.91 us                                                | 6.49 us: 1.37x faster                                                        |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                                       |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                         |
| thrift                  | 1.03 ms                                                | 759 us: 1.36x faster                                                         |
| aiohttp                 | 1.38 ms                                                | 1.02 ms: 1.36x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.95 us: 1.36x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 55.3 ms: 1.36x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                        |
| fannkuch                | 486 ms                                                 | 361 ms: 1.35x faster                                                         |
| tornado_http            | 127 ms                                                 | 94.8 ms: 1.34x faster                                                        |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                         |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                                        |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 645 ms: 1.32x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.2 ms: 1.31x faster                                                        |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                        |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 749 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.8 ms: 1.26x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                                         |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                                        |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                                         |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.21x faster                                                         |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                         |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.5 ms: 1.17x faster                                                        |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.16x faster                                                         |
| json                    | 5.42 ms                                                | 4.66 ms: 1.16x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.4 ms: 1.15x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                        |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                        |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.13 us: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| gc_traversal            | 3.84 ms                                                | 3.65 ms: 1.05x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.70 sec: 1.05x faster                                                       |
| unpickle                | 14.1 us                                                | 13.7 us: 1.04x faster                                                        |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                                        |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                        |
| regex_dna               | 222 ms                                                 | 218 ms: 1.02x faster                                                         |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| async_generators        | 425 ms                                                 | 435 ms: 1.02x slower                                                         |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.42 ms: 1.10x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.11x slower                                                        |
| coverage                | 72.8 ms                                                | 101 ms: 1.39x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, generators
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
