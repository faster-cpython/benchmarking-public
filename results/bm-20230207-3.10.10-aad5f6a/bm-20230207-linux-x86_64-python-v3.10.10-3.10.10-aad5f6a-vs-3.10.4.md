
# Results vs. 3.10.4

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 335 ms: 1.00x faster                                     |
| chameleon      | 9.17 ms                                                | 9.13 ms: 1.00x faster                                    |
| docutils       | 3.18 sec                                               | 3.22 sec: 1.01x slower                                   |
| html5lib       | 85.9 ms                                                | 87.5 ms: 1.02x slower                                    |
| tornado_http   | 128 ms                                                 | 130 ms: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 144 ms                                                 | 137 ms: 1.05x faster                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 24.1 ms: 1.04x faster                                    |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                     |
| regex_effbot   | 3.19 ms                                                | 3.62 ms: 1.13x slower                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                    |
| unpickle_pure_python | 302 us                                                 | 297 us: 1.01x faster                                     |
| xml_etree_parse      | 163 ms                                                 | 161 ms: 1.01x faster                                     |
| xml_etree_generate   | 93.8 ms                                                | 93.0 ms: 1.01x faster                                    |
| pickle_pure_python   | 452 us                                                 | 449 us: 1.01x faster                                     |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.00x faster                                     |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                    |
| json_dumps           | 13.4 ms                                                | 13.6 ms: 1.01x slower                                    |
| json_loads           | 28.7 us                                                | 29.2 us: 1.02x slower                                    |
| unpickle             | 14.2 us                                                | 14.8 us: 1.05x slower                                    |
| pickle_dict          | 27.6 us                                                | 30.5 us: 1.11x slower                                    |
| Geometric mean       | (ref)                                                  | 1.00x slower                                             |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.33 ms: 1.51x faster                                    |
| python_startup_no_site | 5.78 ms                                                | 5.79 ms: 1.00x slower                                    |
| Geometric mean         | (ref)                                                  | 1.23x faster                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 63.7 ms                                                | 62.6 ms: 1.02x faster                                    |
| genshi_text     | 30.6 ms                                                | 30.1 ms: 1.02x faster                                    |
| django_template | 46.3 ms                                                | 46.6 ms: 1.01x slower                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup          | 14.1 ms                                                | 9.33 ms: 1.51x faster                                    |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                    |
| nbody                   | 144 ms                                                 | 137 ms: 1.05x faster                                     |
| coverage                | 74.7 ms                                                | 71.5 ms: 1.05x faster                                    |
| spectral_norm           | 150 ms                                                 | 143 ms: 1.04x faster                                     |
| fannkuch                | 488 ms                                                 | 467 ms: 1.04x faster                                     |
| regex_v8                | 25.0 ms                                                | 24.1 ms: 1.04x faster                                    |
| aiohttp                 | 1.34 ms                                                | 1.29 ms: 1.04x faster                                    |
| richards                | 75.2 ms                                                | 72.6 ms: 1.04x faster                                    |
| deepcopy_memo           | 51.7 us                                                | 49.9 us: 1.03x faster                                    |
| scimark_monte_carlo     | 109 ms                                                 | 105 ms: 1.03x faster                                     |
| scimark_fft             | 421 ms                                                 | 408 ms: 1.03x faster                                     |
| coroutines              | 31.6 ms                                                | 30.6 ms: 1.03x faster                                    |
| bench_thread_pool       | 946 us                                                 | 919 us: 1.03x faster                                     |
| gunicorn                | 1.43 ms                                                | 1.39 ms: 1.03x faster                                    |
| pyflate                 | 676 ms                                                 | 659 ms: 1.03x faster                                     |
| sqlalchemy_imperative   | 21.5 ms                                                | 20.9 ms: 1.03x faster                                    |
| deepcopy                | 438 us                                                 | 428 us: 1.02x faster                                     |
| scimark_sor             | 197 ms                                                 | 193 ms: 1.02x faster                                     |
| genshi_xml              | 63.7 ms                                                | 62.6 ms: 1.02x faster                                    |
| genshi_text             | 30.6 ms                                                | 30.1 ms: 1.02x faster                                    |
| crypto_pyaes            | 117 ms                                                 | 115 ms: 1.02x faster                                     |
| pylint                  | 532 ms                                                 | 524 ms: 1.01x faster                                     |
| unpickle_pure_python    | 302 us                                                 | 297 us: 1.01x faster                                     |
| xml_etree_parse         | 163 ms                                                 | 161 ms: 1.01x faster                                     |
| pathlib                 | 20.0 ms                                                | 19.7 ms: 1.01x faster                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.39 ms: 1.01x faster                                    |
| create_gc_cycles        | 1.65 ms                                                | 1.63 ms: 1.01x faster                                    |
| meteor_contest          | 114 ms                                                 | 113 ms: 1.01x faster                                     |
| sqlglot_parse           | 2.04 ms                                                | 2.03 ms: 1.01x faster                                    |
| xml_etree_generate      | 93.8 ms                                                | 93.0 ms: 1.01x faster                                    |
| raytrace                | 467 ms                                                 | 463 ms: 1.01x faster                                     |
| pickle_pure_python      | 452 us                                                 | 449 us: 1.01x faster                                     |
| dulwich_log             | 75.8 ms                                                | 75.4 ms: 1.01x faster                                    |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                     |
| sqlglot_transpile       | 2.43 ms                                                | 2.41 ms: 1.01x faster                                    |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.00x faster                                     |
| chameleon               | 9.17 ms                                                | 9.13 ms: 1.00x faster                                    |
| generators              | 76.4 ms                                                | 76.1 ms: 1.00x faster                                    |
| 2to3                    | 335 ms                                                 | 335 ms: 1.00x faster                                     |
| sqlglot_optimize        | 65.2 ms                                                | 65.4 ms: 1.00x slower                                    |
| gc_traversal            | 3.53 ms                                                | 3.54 ms: 1.00x slower                                    |
| python_startup_no_site  | 5.78 ms                                                | 5.79 ms: 1.00x slower                                    |
| go                      | 226 ms                                                 | 226 ms: 1.00x slower                                     |
| django_template         | 46.3 ms                                                | 46.6 ms: 1.01x slower                                    |
| deepcopy_reduce         | 3.79 us                                                | 3.81 us: 1.01x slower                                    |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                    |
| chaos                   | 106 ms                                                 | 106 ms: 1.01x slower                                     |
| sqlglot_normalize       | 134 ms                                                 | 136 ms: 1.01x slower                                     |
| json                    | 5.35 ms                                                | 5.40 ms: 1.01x slower                                    |
| json_dumps              | 13.4 ms                                                | 13.6 ms: 1.01x slower                                    |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 167 ms: 1.01x slower                                     |
| sympy_integrate         | 24.0 ms                                                | 24.4 ms: 1.01x slower                                    |
| sympy_str               | 325 ms                                                 | 329 ms: 1.01x slower                                     |
| docutils                | 3.18 sec                                               | 3.22 sec: 1.01x slower                                   |
| tornado_http            | 128 ms                                                 | 130 ms: 1.01x slower                                     |
| sqlite_synth            | 2.92 us                                                | 2.97 us: 1.02x slower                                    |
| pprint_pformat          | 1.98 sec                                               | 2.02 sec: 1.02x slower                                   |
| deltablue               | 7.28 ms                                                | 7.41 ms: 1.02x slower                                    |
| html5lib                | 85.9 ms                                                | 87.5 ms: 1.02x slower                                    |
| json_loads              | 28.7 us                                                | 29.2 us: 1.02x slower                                    |
| pprint_safe_repr        | 953 ms                                                 | 975 ms: 1.02x slower                                     |
| sympy_expand            | 534 ms                                                 | 546 ms: 1.02x slower                                     |
| flaskblogging           | 8.27 ms                                                | 8.47 ms: 1.02x slower                                    |
| mdp                     | 2.74 sec                                               | 2.82 sec: 1.03x slower                                   |
| sympy_sum               | 183 ms                                                 | 189 ms: 1.03x slower                                     |
| logging_simple          | 8.10 us                                                | 8.41 us: 1.04x slower                                    |
| logging_format          | 8.85 us                                                | 9.20 us: 1.04x slower                                    |
| unpickle                | 14.2 us                                                | 14.8 us: 1.05x slower                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 997 ms: 1.05x slower                                     |
| unpack_sequence         | 59.4 ns                                                | 64.0 ns: 1.08x slower                                    |
| pickle_dict             | 27.6 us                                                | 30.5 us: 1.11x slower                                    |
| regex_effbot            | 3.19 ms                                                | 3.62 ms: 1.13x slower                                    |
| Geometric mean          | (ref)                                                  | 1.01x faster                                             |

Benchmark hidden because not significant (21): logging_silent, djangocms, dask, regex_compile, mako, scimark_lu, telco, mypy2, async_generators, hexiom, xml_etree_process, bench_mp_pool, float, asyncio_tcp, async_tree_io, thrift, async_tree_memoization, nqueens, unpickle_list, pycparser, async_tree_none
