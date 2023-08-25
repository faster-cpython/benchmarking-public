
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 264b3dd
- commit date: 2022-07-10
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.30 ms: 1.44x faster                                  |
| html5lib       | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| tornado_http   | 127 ms                                                 | 91.3 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.5 ms: 1.57x faster                                  |
| float          | 111 ms                                                 | 72.4 ms: 1.53x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 126 ms: 1.41x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 53.3 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.9 ms: 1.24x faster                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| json_dumps           | 13.5 ms                                                | 11.8 ms: 1.15x faster                                  |
| pickle_list          | 4.56 us                                                | 4.12 us: 1.11x faster                                  |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.16 ms: 1.74x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.45 ms: 1.56x faster                                  |
| django_template | 45.9 ms                                                | 31.5 ms: 1.46x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                  |
| logging_silent          | 175 ns                                                 | 92.5 ns: 1.89x faster                                  |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.78x faster                                   |
| go                      | 229 ms                                                 | 130 ms: 1.76x faster                                   |
| python_startup          | 14.2 ms                                                | 8.16 ms: 1.74x faster                                  |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.6 ms: 1.67x faster                                  |
| richards                | 74.9 ms                                                | 45.0 ms: 1.66x faster                                  |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.63x faster                                  |
| raytrace                | 464 ms                                                 | 286 ms: 1.62x faster                                   |
| hexiom                  | 9.53 ms                                                | 5.92 ms: 1.61x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.60x faster                                  |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                   |
| scimark_lu              | 163 ms                                                 | 104 ms: 1.57x faster                                   |
| nbody                   | 142 ms                                                 | 90.5 ms: 1.57x faster                                  |
| mako                    | 14.8 ms                                                | 9.45 ms: 1.56x faster                                  |
| spectral_norm           | 150 ms                                                 | 97.7 ms: 1.53x faster                                  |
| float                   | 111 ms                                                 | 72.4 ms: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                   |
| django_template         | 45.9 ms                                                | 31.5 ms: 1.46x faster                                  |
| chameleon               | 9.06 ms                                                | 6.30 ms: 1.44x faster                                  |
| thrift                  | 1.03 ms                                                | 720 us: 1.44x faster                                   |
| logging_simple          | 8.07 us                                                | 5.67 us: 1.42x faster                                  |
| pycparser               | 1.50 sec                                               | 1.06 sec: 1.41x faster                                 |
| regex_compile           | 177 ms                                                 | 126 ms: 1.41x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 53.3 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                  |
| tornado_http            | 127 ms                                                 | 91.3 ms: 1.40x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 46.4 ns: 1.39x faster                                  |
| html5lib                | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                   |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.31x faster                                  |
| fannkuch                | 486 ms                                                 | 378 ms: 1.28x faster                                   |
| dulwich_log             | 75.9 ms                                                | 61.2 ms: 1.24x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.9 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                  |
| sympy_expand            | 545 ms                                                 | 450 ms: 1.21x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                  |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_str               | 328 ms                                                 | 279 ms: 1.18x faster                                   |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.69 ms: 1.16x faster                                  |
| json_dumps              | 13.5 ms                                                | 11.8 ms: 1.15x faster                                  |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.14x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| pickle_list             | 4.56 us                                                | 4.12 us: 1.11x faster                                  |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.08x faster                                   |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x
