
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.33 ms: 1.43x faster                                  |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.41x faster                                  |
| tornado_http   | 127 ms                                                 | 92.4 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 85.1 ms: 1.66x faster                                  |
| float          | 111 ms                                                 | 73.5 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.32 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                   |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                  |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 79.9 ms: 1.18x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| pickle_list          | 4.56 us                                                | 4.31 us: 1.06x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                  |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                  |
| pickle_dict          | 27.3 us                                                | 32.9 us: 1.21x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.91 ms: 1.59x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.60 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.86 ms: 1.50x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| django_template | 45.9 ms                                                | 32.4 ms: 1.42x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 28.0 ms: 2.74x faster                                  |
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                   |
| richards                | 74.9 ms                                                | 40.9 ms: 1.83x faster                                  |
| logging_silent          | 175 ns                                                 | 97.0 ns: 1.80x faster                                  |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.19 ms: 1.72x faster                                  |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                   |
| raytrace                | 464 ms                                                 | 279 ms: 1.67x faster                                   |
| nbody                   | 142 ms                                                 | 85.1 ms: 1.66x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.48 ms: 1.66x faster                                  |
| spectral_norm           | 150 ms                                                 | 91.5 ms: 1.64x faster                                  |
| pyflate                 | 673 ms                                                 | 414 ms: 1.63x faster                                   |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.62x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.94 ms: 1.60x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 67.6 ms: 1.60x faster                                  |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 74.6 ms: 1.59x faster                                  |
| python_startup          | 14.2 ms                                                | 8.91 ms: 1.59x faster                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.53x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.5 ns: 1.52x faster                                  |
| float                   | 111 ms                                                 | 73.5 ms: 1.50x faster                                  |
| mako                    | 14.8 ms                                                | 9.86 ms: 1.50x faster                                  |
| coroutines              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                   |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| chameleon               | 9.06 ms                                                | 6.33 ms: 1.43x faster                                  |
| logging_format          | 8.91 us                                                | 6.22 us: 1.43x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.42x faster                                 |
| django_template         | 45.9 ms                                                | 32.4 ms: 1.42x faster                                  |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.41x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 675 ms: 1.41x faster                                   |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 612 ms: 1.40x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                 |
| async_tree_none         | 717 ms                                                 | 518 ms: 1.39x faster                                   |
| tornado_http            | 127 ms                                                 | 92.4 ms: 1.38x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                  |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                   |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                 |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                  |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                   |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 716 ms: 1.33x faster                                   |
| thrift                  | 1.03 ms                                                | 780 us: 1.32x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                  |
| mypy2                   | 428 ms                                                 | 331 ms: 1.30x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                  |
| fannkuch                | 486 ms                                                 | 378 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                  |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.27x faster                                 |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.26x faster                                  |
| comprehensions          | 26.8 us                                                | 21.5 us: 1.25x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.8 ms: 1.23x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.23x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.4 ms: 1.21x faster                                  |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                   |
| pylint                  | 525 ms                                                 | 435 ms: 1.21x faster                                   |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                   |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                  |
| sympy_str               | 328 ms                                                 | 279 ms: 1.18x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 79.9 ms: 1.18x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.0 ms: 1.18x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                   |
| mdp                     | 2.82 sec                                               | 2.49 sec: 1.13x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                  |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| regex_dna               | 222 ms                                                 | 202 ms: 1.10x faster                                   |
| pickle_list             | 4.56 us                                                | 4.31 us: 1.06x faster                                  |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| async_generators        | 425 ms                                                 | 430 ms: 1.01x slower                                   |
| unpickle_list           | 4.82 us                                                | 4.88 us: 1.01x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.32 ms: 1.03x slower                                  |
| gc_traversal            | 3.84 ms                                                | 3.98 ms: 1.04x slower                                  |
| pickle                  | 10.3 us                                                | 10.9 us: 1.06x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.60 ms: 1.13x slower                                  |
| dask                    | 423 ms                                                 | 492 ms: 1.17x slower                                   |
| pickle_dict             | 27.3 us                                                | 32.9 us: 1.21x slower                                  |
| coverage                | 72.8 ms                                                | 96.0 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (3): telco, bench_mp_pool, unpickle
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
