
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c20186c
- commit date: 2022-07-17
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.28 ms: 1.44x faster                                  |
| html5lib       | 85.9 ms                                                | 62.8 ms: 1.37x faster                                  |
| tornado_http   | 127 ms                                                 | 91.3 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.8 ms: 1.59x faster                                  |
| float          | 111 ms                                                 | 72.0 ms: 1.53x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| regex_dna      | 222 ms                                                 | 197 ms: 1.13x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                   |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 52.2 ms: 1.43x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.2 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| json_dumps           | 13.5 ms                                                | 11.9 ms: 1.14x faster                                  |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.17 ms: 1.73x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.02 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.33 ms: 1.58x faster                                  |
| django_template | 45.9 ms                                                | 32.1 ms: 1.43x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                  |
| logging_silent          | 175 ns                                                 | 91.9 ns: 1.91x faster                                  |
| python_startup          | 14.2 ms                                                | 8.17 ms: 1.73x faster                                  |
| go                      | 229 ms                                                 | 133 ms: 1.73x faster                                   |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                   |
| richards                | 74.9 ms                                                | 44.7 ms: 1.68x faster                                  |
| scimark_sor             | 197 ms                                                 | 117 ms: 1.67x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.1 ms: 1.66x faster                                  |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.9 ms: 1.62x faster                                  |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.61x faster                                  |
| spectral_norm           | 150 ms                                                 | 93.4 ms: 1.61x faster                                  |
| nbody                   | 142 ms                                                 | 88.8 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                   |
| mako                    | 14.8 ms                                                | 9.33 ms: 1.58x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.05 ms: 1.58x faster                                  |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                   |
| float                   | 111 ms                                                 | 72.0 ms: 1.53x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                   |
| chameleon               | 9.06 ms                                                | 6.28 ms: 1.44x faster                                  |
| logging_simple          | 8.07 us                                                | 5.61 us: 1.44x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 52.2 ms: 1.43x faster                                  |
| logging_format          | 8.91 us                                                | 6.22 us: 1.43x faster                                  |
| django_template         | 45.9 ms                                                | 32.1 ms: 1.43x faster                                  |
| pycparser               | 1.50 sec                                               | 1.05 sec: 1.43x faster                                 |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                   |
| tornado_http            | 127 ms                                                 | 91.3 ms: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| html5lib                | 85.9 ms                                                | 62.8 ms: 1.37x faster                                  |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                   |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                  |
| fannkuch                | 486 ms                                                 | 373 ms: 1.30x faster                                   |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.2 ms: 1.25x faster                                  |
| dulwich_log             | 75.9 ms                                                | 60.8 ms: 1.25x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                  |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.21x faster                                   |
| regex_v8                | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| sympy_str               | 328 ms                                                 | 278 ms: 1.18x faster                                   |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                  |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                   |
| json_dumps              | 13.5 ms                                                | 11.9 ms: 1.14x faster                                  |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.13x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                  |
| regex_dna               | 222 ms                                                 | 197 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| telco                   | 6.54 ms                                                | 6.50 ms: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.02 ms: 1.04x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.07x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
