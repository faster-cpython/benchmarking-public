
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: c87e8bd
- commit date: 2023-03-22
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                               |
| chameleon      | 9.06 ms                                                | 6.64 ms: 1.36x faster                                              |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                             |
| html5lib       | 85.9 ms                                                | 61.9 ms: 1.39x faster                                              |
| tornado_http   | 127 ms                                                 | 91.7 ms: 1.39x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.6 ms: 1.56x faster                                              |
| float          | 111 ms                                                 | 74.4 ms: 1.48x faster                                              |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                              |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                               |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.70 ms: 1.40x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 57.3 ms: 1.31x faster                                              |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 81.7 ms: 1.15x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                               |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                               |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                              |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| unpickle_list        | 4.82 us                                                | 5.20 us: 1.08x slower                                              |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                              |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.88 ms: 1.59x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.56 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.48x faster                                              |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                              |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                              |
| genshi_xml      | 63.3 ms                                                | 48.1 ms: 1.32x faster                                              |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                              |
| deltablue               | 7.42 ms                                                | 3.33 ms: 2.23x faster                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                               |
| logging_silent          | 175 ns                                                 | 97.0 ns: 1.81x faster                                              |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                               |
| richards                | 74.9 ms                                                | 44.0 ms: 1.70x faster                                              |
| spectral_norm           | 150 ms                                                 | 90.4 ms: 1.66x faster                                              |
| pyflate                 | 673 ms                                                 | 417 ms: 1.61x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 67.8 ms: 1.60x faster                                              |
| python_startup          | 14.2 ms                                                | 8.88 ms: 1.59x faster                                              |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.59x faster                                              |
| raytrace                | 464 ms                                                 | 293 ms: 1.58x faster                                               |
| hexiom                  | 9.53 ms                                                | 6.04 ms: 1.58x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 75.3 ms: 1.57x faster                                              |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                               |
| nbody                   | 142 ms                                                 | 90.6 ms: 1.56x faster                                              |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                              |
| float                   | 111 ms                                                 | 74.4 ms: 1.48x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                               |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.48x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 44.0 ns: 1.47x faster                                              |
| coroutines              | 31.8 ms                                                | 22.5 ms: 1.41x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.46 ms: 1.41x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.40x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.70 ms: 1.40x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.39x faster                                             |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                              |
| tornado_http            | 127 ms                                                 | 91.7 ms: 1.39x faster                                              |
| html5lib                | 85.9 ms                                                | 61.9 ms: 1.39x faster                                              |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                              |
| scimark_fft             | 424 ms                                                 | 307 ms: 1.38x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 693 ms: 1.38x faster                                               |
| logging_format          | 8.91 us                                                | 6.47 us: 1.38x faster                                              |
| logging_simple          | 8.07 us                                                | 5.90 us: 1.37x faster                                              |
| chameleon               | 9.06 ms                                                | 6.64 ms: 1.36x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                             |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.36x faster                                               |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                               |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                               |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| genshi_xml              | 63.3 ms                                                | 48.1 ms: 1.32x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 57.3 ms: 1.31x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                              |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.22 ms: 1.29x faster                                              |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.29x faster                                             |
| async_tree_memoization  | 854 ms                                                 | 667 ms: 1.28x faster                                               |
| mypy2                   | 428 ms                                                 | 336 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 746 ms: 1.28x faster                                               |
| thrift                  | 1.03 ms                                                | 816 us: 1.27x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 52.2 ms: 1.25x faster                                              |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                              |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                             |
| dulwich_log             | 75.9 ms                                                | 63.4 ms: 1.20x faster                                              |
| bench_thread_pool       | 947 us                                                 | 794 us: 1.19x faster                                               |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                              |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                              |
| sympy_expand            | 545 ms                                                 | 465 ms: 1.17x faster                                               |
| sympy_str               | 328 ms                                                 | 284 ms: 1.15x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 81.7 ms: 1.15x faster                                              |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                              |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                              |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                               |
| comprehensions          | 26.8 us                                                | 24.4 us: 1.10x faster                                              |
| regex_v8                | 25.0 ms                                                | 22.8 ms: 1.10x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                               |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                               |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.08x faster                                               |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                               |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                              |
| async_generators        | 425 ms                                                 | 417 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| gc_traversal            | 3.84 ms                                                | 3.98 ms: 1.04x slower                                              |
| unpickle_list           | 4.82 us                                                | 5.20 us: 1.08x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.56 ms: 1.13x slower                                              |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                              |
| dask                    | 423 ms                                                 | 509 ms: 1.21x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (2): telco, bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
