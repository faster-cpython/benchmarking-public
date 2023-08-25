
# Results vs. 3.10.4

- fork: python
- ref: 2cdc5189a6bc3157fddd
- machine: linux-x86_64
- commit hash: 2cdc518
- commit date: 2023-03-26
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                  |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                 |
| html5lib       | 85.9 ms                                                | 62.3 ms: 1.38x faster                                                  |
| tornado_http   | 127 ms                                                 | 91.1 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.8 ms: 1.61x faster                                                  |
| float          | 111 ms                                                 | 73.9 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.57 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.3 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.5 ms: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.27 us: 1.07x faster                                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.79 ms: 1.61x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.6 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230326-linux-x86_64-python-2cdc5189a6bc3157fddd-3.12.0a6+-2cdc518 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                   |
| logging_silent          | 175 ns                                                 | 96.5 ns: 1.81x faster                                                  |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                                   |
| richards                | 74.9 ms                                                | 43.5 ms: 1.72x faster                                                  |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                   |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                   |
| nbody                   | 142 ms                                                 | 87.8 ms: 1.61x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.79 ms: 1.61x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 74.0 ms: 1.60x faster                                                  |
| pyflate                 | 673 ms                                                 | 421 ms: 1.60x faster                                                   |
| chaos                   | 106 ms                                                 | 66.5 ms: 1.60x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 67.8 ms: 1.60x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                   |
| spectral_norm           | 150 ms                                                 | 94.0 ms: 1.60x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.01 ms: 1.59x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.54x faster                                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                   |
| float                   | 111 ms                                                 | 73.9 ms: 1.50x faster                                                  |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 43.7 ns: 1.48x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                 |
| logging_simple          | 8.07 us                                                | 5.68 us: 1.42x faster                                                  |
| logging_format          | 8.91 us                                                | 6.28 us: 1.42x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.57 ms: 1.41x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| tornado_http            | 127 ms                                                 | 91.1 ms: 1.40x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                   |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                  |
| html5lib                | 85.9 ms                                                | 62.3 ms: 1.38x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                 |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.38x faster                                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                   |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| coroutines              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 47.6 ms: 1.33x faster                                                  |
| thrift                  | 1.03 ms                                                | 780 us: 1.32x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 652 ms: 1.31x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                  |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.17 sec: 1.28x faster                                                 |
| fannkuch                | 486 ms                                                 | 380 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 746 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 107 ms: 1.26x faster                                                   |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                 |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.21x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 789 us: 1.20x faster                                                   |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                  |
| sympy_expand            | 545 ms                                                 | 463 ms: 1.18x faster                                                   |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.3 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                  |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 99.5 ms: 1.12x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                   |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.27 us: 1.07x faster                                                  |
| async_generators        | 425 ms                                                 | 408 ms: 1.04x faster                                                   |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| telco                   | 6.54 ms                                                | 6.67 ms: 1.02x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 4.31 ms: 1.12x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                  |
| dask                    | 423 ms                                                 | 511 ms: 1.21x slower                                                   |
| coverage                | 72.8 ms                                                | 95.5 ms: 1.31x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
