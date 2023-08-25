
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_call_more
- machine: linux-x86_64
- commit hash: d02b607
- commit date: 2023-04-04
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.67 ms: 1.36x faster                                                    |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                   |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                    |
| tornado_http   | 127 ms                                                 | 90.8 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.1 ms: 1.61x faster                                                    |
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                                    |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                    |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.69 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.43x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                    |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 82.1 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 99.9 ms: 1.12x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.36 us: 1.05x faster                                                    |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                    |
| unpickle_list        | 4.82 us                                                | 5.17 us: 1.07x slower                                                    |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.78 ms: 1.61x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.11x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.45x faster                                                    |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                    |
| django_template | 45.9 ms                                                | 33.8 ms: 1.36x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                    |
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.28x faster                                                    |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                     |
| logging_silent          | 175 ns                                                 | 98.3 ns: 1.78x faster                                                    |
| richards                | 74.9 ms                                                | 43.5 ms: 1.72x faster                                                    |
| scimark_sor             | 197 ms                                                 | 116 ms: 1.69x faster                                                     |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                                     |
| raytrace                | 464 ms                                                 | 279 ms: 1.66x faster                                                     |
| chaos                   | 106 ms                                                 | 65.8 ms: 1.61x faster                                                    |
| python_startup          | 14.2 ms                                                | 8.78 ms: 1.61x faster                                                    |
| nbody                   | 142 ms                                                 | 88.1 ms: 1.61x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                     |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 68.6 ms: 1.58x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.3 ms: 1.57x faster                                                    |
| hexiom                  | 9.53 ms                                                | 6.16 ms: 1.55x faster                                                    |
| pyflate                 | 673 ms                                                 | 441 ms: 1.53x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.53x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                    |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                     |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                                    |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.45x faster                                                    |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.43x faster                                                    |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                    |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                    |
| logging_format          | 8.91 us                                                | 6.34 us: 1.41x faster                                                    |
| tornado_http            | 127 ms                                                 | 90.8 ms: 1.40x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.76 us: 1.40x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.40x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                   |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 695 ms: 1.37x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                    |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.67 ms: 1.36x faster                                                    |
| django_template         | 45.9 ms                                                | 33.8 ms: 1.36x faster                                                    |
| coroutines              | 31.8 ms                                                | 23.5 ms: 1.36x faster                                                    |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.35x faster                                                     |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                     |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                     |
| xml_etree_process       | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                    |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                     |
| thrift                  | 1.03 ms                                                | 783 us: 1.32x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                                    |
| async_tree_cpu_io_mixed | 951 ms                                                 | 734 ms: 1.30x faster                                                     |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                    |
| fannkuch                | 486 ms                                                 | 388 ms: 1.25x faster                                                     |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                     |
| nqueens                 | 100 ms                                                 | 82.7 ms: 1.21x faster                                                    |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                     |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.19x faster                                                    |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                                    |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                    |
| sympy_expand            | 545 ms                                                 | 464 ms: 1.18x faster                                                     |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                                    |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                    |
| xml_etree_generate      | 94.2 ms                                                | 82.1 ms: 1.15x faster                                                    |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                    |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                                    |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 99.9 ms: 1.12x faster                                                    |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                     |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.66 us: 1.10x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                     |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                     |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.36 us: 1.05x faster                                                    |
| async_generators        | 425 ms                                                 | 417 ms: 1.02x faster                                                     |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                    |
| unpickle_list           | 4.82 us                                                | 5.17 us: 1.07x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.11x slower                                                    |
| gc_traversal            | 3.84 ms                                                | 4.32 ms: 1.12x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.69 ms: 1.14x slower                                                    |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                                    |
| dask                    | 423 ms                                                 | 510 ms: 1.21x slower                                                     |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
