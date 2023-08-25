
# Results vs. 3.10.4

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x faster \*
- HPT reliability: 97.32%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 335 ms: 1.00x faster                                     |
| chameleon      | 9.06 ms                                                | 9.13 ms: 1.01x slower                                    |
| docutils       | 3.17 sec                                               | 3.22 sec: 1.02x slower                                   |
| html5lib       | 85.9 ms                                                | 87.5 ms: 1.02x slower                                    |
| tornado_http   | 127 ms                                                 | 130 ms: 1.02x slower                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 142 ms                                                 | 137 ms: 1.03x faster                                     |
| float          | 111 ms                                                 | 109 ms: 1.01x faster                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 24.1 ms: 1.04x faster                                    |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                     |
| regex_effbot   | 3.23 ms                                                | 3.62 ms: 1.12x slower                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                    |
| pickle_pure_python   | 455 us                                                 | 449 us: 1.01x faster                                     |
| xml_etree_parse      | 163 ms                                                 | 161 ms: 1.01x faster                                     |
| xml_etree_generate   | 94.2 ms                                                | 93.0 ms: 1.01x faster                                    |
| unpickle_pure_python | 300 us                                                 | 297 us: 1.01x faster                                     |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.01x faster                                     |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                    |
| xml_etree_process    | 74.9 ms                                                | 74.4 ms: 1.01x faster                                    |
| json_dumps           | 13.5 ms                                                | 13.6 ms: 1.01x slower                                    |
| json_loads           | 28.8 us                                                | 29.2 us: 1.02x slower                                    |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                    |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                    |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                    |
| Geometric mean       | (ref)                                                  | 1.00x slower                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                    |
| python_startup_no_site | 5.82 ms                                                | 5.79 ms: 1.00x faster                                    |
| Geometric mean         | (ref)                                                  | 1.23x faster                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                | 62.6 ms: 1.01x faster                                    |
| mako            | 14.8 ms                                                | 14.6 ms: 1.01x faster                                    |
| genshi_text     | 30.3 ms                                                | 30.1 ms: 1.01x faster                                    |
| django_template | 45.9 ms                                                | 46.6 ms: 1.01x slower                                    |
| Geometric mean  | (ref)                                                  | 1.00x faster                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup          | 14.2 ms                                                | 9.33 ms: 1.52x faster                                    |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                    |
| gc_traversal            | 3.84 ms                                                | 3.54 ms: 1.09x faster                                    |
| aiohttp                 | 1.38 ms                                                | 1.29 ms: 1.07x faster                                    |
| deepcopy_memo           | 52.3 us                                                | 49.9 us: 1.05x faster                                    |
| gunicorn                | 1.46 ms                                                | 1.39 ms: 1.05x faster                                    |
| spectral_norm           | 150 ms                                                 | 143 ms: 1.05x faster                                     |
| fannkuch                | 486 ms                                                 | 467 ms: 1.04x faster                                     |
| coroutines              | 31.8 ms                                                | 30.6 ms: 1.04x faster                                    |
| scimark_fft             | 424 ms                                                 | 408 ms: 1.04x faster                                     |
| regex_v8                | 25.0 ms                                                | 24.1 ms: 1.04x faster                                    |
| nbody                   | 142 ms                                                 | 137 ms: 1.03x faster                                     |
| deepcopy                | 442 us                                                 | 428 us: 1.03x faster                                     |
| richards                | 74.9 ms                                                | 72.6 ms: 1.03x faster                                    |
| crypto_pyaes            | 118 ms                                                 | 115 ms: 1.03x faster                                     |
| scimark_monte_carlo     | 108 ms                                                 | 105 ms: 1.03x faster                                     |
| bench_thread_pool       | 947 us                                                 | 919 us: 1.03x faster                                     |
| regex_dna               | 222 ms                                                 | 216 ms: 1.03x faster                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.63 ms: 1.02x faster                                    |
| pyflate                 | 673 ms                                                 | 659 ms: 1.02x faster                                     |
| scimark_sor             | 197 ms                                                 | 193 ms: 1.02x faster                                     |
| scimark_lu              | 163 ms                                                 | 160 ms: 1.02x faster                                     |
| coverage                | 72.8 ms                                                | 71.5 ms: 1.02x faster                                    |
| meteor_contest          | 115 ms                                                 | 113 ms: 1.02x faster                                     |
| sqlglot_parse           | 2.06 ms                                                | 2.03 ms: 1.02x faster                                    |
| pickle_pure_python      | 455 us                                                 | 449 us: 1.01x faster                                     |
| float                   | 111 ms                                                 | 109 ms: 1.01x faster                                     |
| pathlib                 | 20.0 ms                                                | 19.7 ms: 1.01x faster                                    |
| sqlglot_transpile       | 2.45 ms                                                | 2.41 ms: 1.01x faster                                    |
| xml_etree_parse         | 163 ms                                                 | 161 ms: 1.01x faster                                     |
| go                      | 229 ms                                                 | 226 ms: 1.01x faster                                     |
| xml_etree_generate      | 94.2 ms                                                | 93.0 ms: 1.01x faster                                    |
| unpack_sequence         | 64.7 ns                                                | 64.0 ns: 1.01x faster                                    |
| hexiom                  | 9.53 ms                                                | 9.42 ms: 1.01x faster                                    |
| genshi_xml              | 63.3 ms                                                | 62.6 ms: 1.01x faster                                    |
| asyncio_tcp             | 925 ms                                                 | 915 ms: 1.01x faster                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.39 ms: 1.01x faster                                    |
| mako                    | 14.8 ms                                                | 14.6 ms: 1.01x faster                                    |
| unpickle_pure_python    | 300 us                                                 | 297 us: 1.01x faster                                     |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.01x faster                                     |
| generators              | 76.8 ms                                                | 76.1 ms: 1.01x faster                                    |
| genshi_text             | 30.3 ms                                                | 30.1 ms: 1.01x faster                                    |
| dulwich_log             | 75.9 ms                                                | 75.4 ms: 1.01x faster                                    |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                    |
| xml_etree_process       | 74.9 ms                                                | 74.4 ms: 1.01x faster                                    |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                     |
| python_startup_no_site  | 5.82 ms                                                | 5.79 ms: 1.00x faster                                    |
| 2to3                    | 336 ms                                                 | 335 ms: 1.00x faster                                     |
| sympy_integrate         | 24.3 ms                                                | 24.4 ms: 1.00x slower                                    |
| json_dumps              | 13.5 ms                                                | 13.6 ms: 1.01x slower                                    |
| chameleon               | 9.06 ms                                                | 9.13 ms: 1.01x slower                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 167 ms: 1.01x slower                                     |
| sqlite_synth            | 2.93 us                                                | 2.97 us: 1.01x slower                                    |
| django_template         | 45.9 ms                                                | 46.6 ms: 1.01x slower                                    |
| json_loads              | 28.8 us                                                | 29.2 us: 1.02x slower                                    |
| docutils                | 3.17 sec                                               | 3.22 sec: 1.02x slower                                   |
| pprint_pformat          | 1.99 sec                                               | 2.02 sec: 1.02x slower                                   |
| html5lib                | 85.9 ms                                                | 87.5 ms: 1.02x slower                                    |
| pprint_safe_repr        | 955 ms                                                 | 975 ms: 1.02x slower                                     |
| tornado_http            | 127 ms                                                 | 130 ms: 1.02x slower                                     |
| sympy_sum               | 185 ms                                                 | 189 ms: 1.02x slower                                     |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.02x slower                                    |
| pycparser               | 1.50 sec                                               | 1.54 sec: 1.02x slower                                   |
| flaskblogging           | 8.27 ms                                                | 8.47 ms: 1.02x slower                                    |
| telco                   | 6.54 ms                                                | 6.71 ms: 1.03x slower                                    |
| dask                    | 423 ms                                                 | 434 ms: 1.03x slower                                     |
| logging_format          | 8.91 us                                                | 9.20 us: 1.03x slower                                    |
| logging_simple          | 8.07 us                                                | 8.41 us: 1.04x slower                                    |
| unpickle                | 14.1 us                                                | 14.8 us: 1.05x slower                                    |
| async_tree_cpu_io_mixed | 951 ms                                                 | 997 ms: 1.05x slower                                     |
| pickle_dict             | 27.3 us                                                | 30.5 us: 1.12x slower                                    |
| regex_effbot            | 3.23 ms                                                | 3.62 ms: 1.12x slower                                    |
| Geometric mean          | (ref)                                                  | 1.01x faster                                             |

Benchmark hidden because not significant (23): sqlalchemy_imperative, logging_silent, deepcopy_reduce, json, raytrace, regex_compile, mdp, deltablue, pylint, bench_mp_pool, sqlglot_optimize, chaos, async_generators, thrift, mypy2, sympy_expand, sympy_str, nqueens, async_tree_memoization, sqlglot_normalize, async_tree_io, async_tree_none, djangocms
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 97.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
