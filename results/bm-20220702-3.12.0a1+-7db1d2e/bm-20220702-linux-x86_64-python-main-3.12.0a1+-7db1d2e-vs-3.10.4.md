
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7db1d2e
- commit date: 2022-07-02
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.36x faster                                   |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                  |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                  |
| tornado_http   | 127 ms                                                 | 91.4 ms: 1.39x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 69.9 ms: 1.58x faster                                  |
| nbody          | 142 ms                                                 | 89.9 ms: 1.57x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 125 ms: 1.42x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 197 ms: 1.13x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.49 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 52.0 ms: 1.44x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.0 ms: 1.26x faster                                  |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| json_dumps           | 13.5 ms                                                | 11.9 ms: 1.13x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle_list          | 4.56 us                                                | 4.28 us: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.22 ms: 1.72x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.07 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.55 ms: 1.55x faster                                  |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                  |
| Geometric mean  | (ref)                                                  | 1.49x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                  |
| logging_silent          | 175 ns                                                 | 91.7 ns: 1.91x faster                                  |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                   |
| go                      | 229 ms                                                 | 130 ms: 1.76x faster                                   |
| pyflate                 | 673 ms                                                 | 389 ms: 1.73x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 62.8 ms: 1.72x faster                                  |
| python_startup          | 14.2 ms                                                | 8.22 ms: 1.72x faster                                  |
| richards                | 74.9 ms                                                | 44.6 ms: 1.68x faster                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                   |
| chaos                   | 106 ms                                                 | 65.2 ms: 1.63x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.88 ms: 1.62x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                  |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                   |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                  |
| float                   | 111 ms                                                 | 69.9 ms: 1.58x faster                                  |
| nbody                   | 142 ms                                                 | 89.9 ms: 1.57x faster                                  |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.56x faster                                   |
| mako                    | 14.8 ms                                                | 9.55 ms: 1.55x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 52.0 ms: 1.44x faster                                  |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 45.5 ns: 1.42x faster                                  |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                  |
| regex_compile           | 177 ms                                                 | 125 ms: 1.42x faster                                   |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                  |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                  |
| tornado_http            | 127 ms                                                 | 91.4 ms: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                 |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                  |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                   |
| 2to3                    | 336 ms                                                 | 248 ms: 1.36x faster                                   |
| fannkuch                | 486 ms                                                 | 373 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.21 ms: 1.29x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.0 ms: 1.26x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.2 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.23x faster                                  |
| sympy_expand            | 545 ms                                                 | 450 ms: 1.21x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                  |
| sympy_str               | 328 ms                                                 | 276 ms: 1.19x faster                                   |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                   |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                  |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.13x faster                                   |
| json_dumps              | 13.5 ms                                                | 11.9 ms: 1.13x faster                                  |
| regex_dna               | 222 ms                                                 | 197 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle_list             | 4.56 us                                                | 4.28 us: 1.07x faster                                  |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.07 ms: 1.04x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.49 ms: 1.08x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.12x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x
