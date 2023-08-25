
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 87449dc
- commit date: 2023-03-07
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                      |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                      |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.6 ms: 1.55x faster                                                      |
| float          | 111 ms                                                 | 74.3 ms: 1.49x faster                                                      |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                      |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 55.6 ms: 1.35x faster                                                      |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.18 us: 1.09x faster                                                      |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                                      |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                      |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                                      |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.99 ms: 1.57x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.47x faster                                                      |
| genshi_text     | 30.3 ms                                                | 21.9 ms: 1.38x faster                                                      |
| django_template | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 48.9 ms: 1.30x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.9 ms: 2.49x faster                                                      |
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                      |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 508 ms: 1.82x faster                                                       |
| logging_silent          | 175 ns                                                 | 96.4 ns: 1.82x faster                                                      |
| richards                | 74.9 ms                                                | 43.4 ms: 1.73x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.63x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 66.8 ms: 1.62x faster                                                      |
| go                      | 229 ms                                                 | 142 ms: 1.62x faster                                                       |
| pyflate                 | 673 ms                                                 | 418 ms: 1.61x faster                                                       |
| raytrace                | 464 ms                                                 | 289 ms: 1.61x faster                                                       |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.58x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.99 ms: 1.57x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                                       |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.56x faster                                                      |
| nbody                   | 142 ms                                                 | 91.6 ms: 1.55x faster                                                      |
| hexiom                  | 9.53 ms                                                | 6.20 ms: 1.54x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                                       |
| float                   | 111 ms                                                 | 74.3 ms: 1.49x faster                                                      |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                                       |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.47x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 45.2 ns: 1.43x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.43x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.47 ms: 1.40x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.77 ms: 1.39x faster                                                      |
| genshi_text             | 30.3 ms                                                | 21.9 ms: 1.38x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.88 us: 1.37x faster                                                      |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                       |
| django_template         | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                      |
| coroutines              | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 700 ms: 1.36x faster                                                       |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                                     |
| logging_format          | 8.91 us                                                | 6.58 us: 1.35x faster                                                      |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 55.6 ms: 1.35x faster                                                      |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                                      |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                       |
| fannkuch                | 486 ms                                                 | 367 ms: 1.32x faster                                                       |
| thrift                  | 1.03 ms                                                | 784 us: 1.32x faster                                                       |
| deepcopy                | 442 us                                                 | 337 us: 1.31x faster                                                       |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 48.9 ms: 1.30x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                       |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 748 ms: 1.27x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 3.04 us: 1.26x faster                                                      |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.50 ms: 1.21x faster                                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                       |
| nqueens                 | 100 ms                                                 | 83.0 ms: 1.20x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 794 us: 1.19x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                                      |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                      |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                                      |
| sympy_expand            | 545 ms                                                 | 466 ms: 1.17x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                      |
| sympy_str               | 328 ms                                                 | 286 ms: 1.15x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                      |
| comprehensions          | 26.8 us                                                | 24.0 us: 1.12x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                      |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                       |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                                       |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.18 us: 1.09x faster                                                      |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                                      |
| async_generators        | 425 ms                                                 | 415 ms: 1.02x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                                      |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                      |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.13 us: 1.06x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                      |
| pickle_dict             | 27.3 us                                                | 31.2 us: 1.14x slower                                                      |
| dask                    | 423 ms                                                 | 512 ms: 1.21x slower                                                       |
| coverage                | 72.8 ms                                                | 94.4 ms: 1.30x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (2): telco, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
