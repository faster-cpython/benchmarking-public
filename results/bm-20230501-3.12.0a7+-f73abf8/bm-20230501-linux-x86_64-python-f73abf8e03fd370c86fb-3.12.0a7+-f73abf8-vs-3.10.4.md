
# Results vs. 3.10.4

- fork: python
- ref: f73abf8e03fd370c86fb
- machine: linux-x86_64
- commit hash: f73abf8
- commit date: 2023-05-01
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.25x faster                                                   |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                 |
| html5lib       | 85.9 ms                                                | 65.0 ms: 1.32x faster                                                  |
| tornado_http   | 127 ms                                                 | 98.5 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.2 ms: 1.59x faster                                                  |
| float          | 111 ms                                                 | 82.0 ms: 1.35x faster                                                  |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 319 us: 1.43x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                                   |
| json_dumps           | 13.5 ms                                                | 10.1 ms: 1.35x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 58.2 ms: 1.29x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.0 ms: 1.12x faster                                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.79 us: 1.05x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.19 us: 1.08x slower                                                  |
| unpickle             | 14.1 us                                                | 15.7 us: 1.11x slower                                                  |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.06 ms: 1.56x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.65 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                  |
| genshi_text    | 30.3 ms                                                | 22.7 ms: 1.34x faster                                                  |
| genshi_xml     | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.0 ms: 2.47x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.54 ms: 2.09x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 511 ms: 1.81x faster                                                   |
| logging_silent          | 175 ns                                                 | 101 ns: 1.73x faster                                                   |
| richards                | 74.9 ms                                                | 43.3 ms: 1.73x faster                                                  |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                   |
| nbody                   | 142 ms                                                 | 89.2 ms: 1.59x faster                                                  |
| python_startup          | 14.2 ms                                                | 9.06 ms: 1.56x faster                                                  |
| scimark_sor             | 197 ms                                                 | 126 ms: 1.56x faster                                                   |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.55x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.22 ms: 1.53x faster                                                  |
| pyflate                 | 673 ms                                                 | 444 ms: 1.51x faster                                                   |
| raytrace                | 464 ms                                                 | 306 ms: 1.51x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 79.5 ms: 1.49x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 73.0 ms: 1.48x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                  |
| spectral_norm           | 150 ms                                                 | 102 ms: 1.46x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                 |
| async_tree_none         | 717 ms                                                 | 499 ms: 1.44x faster                                                   |
| scimark_lu              | 163 ms                                                 | 114 ms: 1.43x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 319 us: 1.43x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 614 ms: 1.39x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 217 us: 1.38x faster                                                   |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                  |
| mako                    | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 47.5 ns: 1.36x faster                                                  |
| float                   | 111 ms                                                 | 82.0 ms: 1.35x faster                                                  |
| json_dumps              | 13.5 ms                                                | 10.1 ms: 1.35x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 39.0 us: 1.34x faster                                                  |
| genshi_text             | 30.3 ms                                                | 22.7 ms: 1.34x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.33x faster                                                 |
| html5lib                | 85.9 ms                                                | 65.0 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 722 ms: 1.32x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 733 ms: 1.30x faster                                                   |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                                   |
| tornado_http            | 127 ms                                                 | 98.5 ms: 1.29x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 58.2 ms: 1.29x faster                                                  |
| logging_simple          | 8.07 us                                                | 6.28 us: 1.29x faster                                                  |
| logging_format          | 8.91 us                                                | 6.95 us: 1.28x faster                                                  |
| thrift                  | 1.03 ms                                                | 811 us: 1.27x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                  |
| 2to3                    | 336 ms                                                 | 268 ms: 1.25x faster                                                   |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                                  |
| regex_compile           | 177 ms                                                 | 144 ms: 1.23x faster                                                   |
| mypy2                   | 428 ms                                                 | 349 ms: 1.23x faster                                                   |
| deepcopy                | 442 us                                                 | 363 us: 1.22x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.21x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 54.5 ms: 1.20x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.20 us: 1.20x faster                                                  |
| scimark_fft             | 424 ms                                                 | 356 ms: 1.19x faster                                                   |
| docutils                | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.15x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 834 us: 1.14x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.7 ms: 1.13x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.83 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 67.7 ms: 1.12x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 84.0 ms: 1.12x faster                                                  |
| json_loads              | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| json                    | 5.42 ms                                                | 4.98 ms: 1.09x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| meteor_contest          | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.94 ms: 1.02x slower                                                  |
| telco                   | 6.54 ms                                                | 6.76 ms: 1.03x slower                                                  |
| async_generators        | 425 ms                                                 | 442 ms: 1.04x slower                                                   |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| pickle_list             | 4.56 us                                                | 4.79 us: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.19 us: 1.08x slower                                                  |
| unpickle                | 14.1 us                                                | 15.7 us: 1.11x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.65 ms: 1.14x slower                                                  |
| pickle_dict             | 27.3 us                                                | 32.3 us: 1.18x slower                                                  |
| dask                    | 423 ms                                                 | 539 ms: 1.28x slower                                                   |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
