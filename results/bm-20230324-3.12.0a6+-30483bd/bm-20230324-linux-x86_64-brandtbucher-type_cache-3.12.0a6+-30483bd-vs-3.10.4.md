
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 30483bd
- commit date: 2023-03-24
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                               |
| chameleon      | 9.06 ms                                                | 6.54 ms: 1.39x faster                                              |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                             |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                              |
| tornado_http   | 127 ms                                                 | 92.2 ms: 1.38x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.6 ms: 1.62x faster                                              |
| float          | 111 ms                                                 | 73.6 ms: 1.50x faster                                              |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                              |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                               |
| unpickle_pure_python | 300 us                                                 | 204 us: 1.48x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.86 ms: 1.37x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 56.4 ms: 1.33x faster                                              |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 81.4 ms: 1.16x faster                                              |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                               |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                              |
| unpickle_list        | 4.82 us                                                | 5.12 us: 1.06x slower                                              |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.18x slower                                              |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                       |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.85 ms: 1.60x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                              |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                              |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                              |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                              |
| genshi_xml      | 63.3 ms                                                | 48.2 ms: 1.31x faster                                              |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                              |
| deltablue               | 7.42 ms                                                | 3.31 ms: 2.24x faster                                              |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 510 ms: 1.81x faster                                               |
| logging_silent          | 175 ns                                                 | 96.6 ns: 1.81x faster                                              |
| richards                | 74.9 ms                                                | 43.0 ms: 1.74x faster                                              |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                               |
| spectral_norm           | 150 ms                                                 | 91.5 ms: 1.64x faster                                              |
| nbody                   | 142 ms                                                 | 87.6 ms: 1.62x faster                                              |
| pyflate                 | 673 ms                                                 | 418 ms: 1.61x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 67.4 ms: 1.61x faster                                              |
| python_startup          | 14.2 ms                                                | 8.85 ms: 1.60x faster                                              |
| raytrace                | 464 ms                                                 | 290 ms: 1.60x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 74.1 ms: 1.60x faster                                              |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.59x faster                                              |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                               |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                              |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                              |
| float                   | 111 ms                                                 | 73.6 ms: 1.50x faster                                              |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 204 us: 1.48x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 45.2 ns: 1.43x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                              |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.40x faster                                              |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                             |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                              |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                              |
| chameleon               | 9.06 ms                                                | 6.54 ms: 1.39x faster                                              |
| tornado_http            | 127 ms                                                 | 92.2 ms: 1.38x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 692 ms: 1.38x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.86 ms: 1.37x faster                                              |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                              |
| logging_format          | 8.91 us                                                | 6.54 us: 1.36x faster                                              |
| logging_simple          | 8.07 us                                                | 5.94 us: 1.36x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                              |
| async_tree_none         | 717 ms                                                 | 531 ms: 1.35x faster                                               |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                               |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 56.4 ms: 1.33x faster                                              |
| genshi_xml              | 63.3 ms                                                | 48.2 ms: 1.31x faster                                              |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                              |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.29x faster                                             |
| thrift                  | 1.03 ms                                                | 805 us: 1.28x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                               |
| fannkuch                | 486 ms                                                 | 381 ms: 1.28x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.28x faster                                               |
| mypy2                   | 428 ms                                                 | 336 ms: 1.27x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.7 ms: 1.26x faster                                              |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                             |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                              |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                              |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                              |
| bench_thread_pool       | 947 us                                                 | 798 us: 1.19x faster                                               |
| dulwich_log             | 75.9 ms                                                | 64.1 ms: 1.18x faster                                              |
| sympy_expand            | 545 ms                                                 | 465 ms: 1.17x faster                                               |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 81.4 ms: 1.16x faster                                              |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                              |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                              |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                              |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                               |
| comprehensions          | 26.8 us                                                | 24.3 us: 1.11x faster                                              |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                               |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                               |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                              |
| mdp                     | 2.82 sec                                               | 2.71 sec: 1.04x faster                                             |
| async_generators        | 425 ms                                                 | 416 ms: 1.02x faster                                               |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                              |
| unpickle_list           | 4.82 us                                                | 5.12 us: 1.06x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.53 ms: 1.09x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                              |
| pickle_dict             | 27.3 us                                                | 32.3 us: 1.18x slower                                              |
| dask                    | 423 ms                                                 | 516 ms: 1.22x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
