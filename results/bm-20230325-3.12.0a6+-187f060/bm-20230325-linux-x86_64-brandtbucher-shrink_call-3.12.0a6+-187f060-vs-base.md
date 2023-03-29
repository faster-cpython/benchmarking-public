
# Results vs. base

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 187f060
- commit date: 2023-03-25
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| chameleon      | 6.42 ms                                                                | 6.48 ms: 1.01x slower                                               |
| docutils       | 2.53 sec                                                               | 2.56 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 90.6 ms                                                                | 88.2 ms: 1.03x faster                                               |
| float          | 73.6 ms                                                                | 74.4 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.38 ms                                                                | 3.64 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 4.37 us                                                                | 4.21 us: 1.04x faster                                               |
| pickle_dict          | 32.1 us                                                                | 31.5 us: 1.02x faster                                               |
| pickle               | 10.4 us                                                                | 10.3 us: 1.01x faster                                               |
| xml_etree_process    | 55.7 ms                                                                | 55.3 ms: 1.01x faster                                               |
| unpickle_pure_python | 204 us                                                                 | 202 us: 1.01x faster                                                |
| json_dumps           | 9.53 ms                                                                | 9.62 ms: 1.01x slower                                               |
| pickle_pure_python   | 284 us                                                                 | 289 us: 1.01x slower                                                |
| unpickle_list        | 5.06 us                                                                | 5.17 us: 1.02x slower                                               |
| xml_etree_iterparse  | 101 ms                                                                 | 103 ms: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): json_loads, xml_etree_generate, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.52 ms                                                                | 6.53 ms: 1.00x slower                                               |
| python_startup         | 8.82 ms                                                                | 8.83 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 10.0 ms                                                                | 10.0 ms: 1.00x faster                                               |
| django_template | 32.5 ms                                                                | 32.8 ms: 1.01x slower                                               |
| genshi_xml      | 47.1 ms                                                                | 48.6 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6+-e375bff | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal            | 4.07 ms                                                                | 3.54 ms: 1.15x faster                                               |
| logging_format          | 6.56 us                                                                | 6.23 us: 1.05x faster                                               |
| scimark_fft             | 317 ms                                                                 | 304 ms: 1.04x faster                                                |
| pickle_list             | 4.37 us                                                                | 4.21 us: 1.04x faster                                               |
| logging_simple          | 5.87 us                                                                | 5.68 us: 1.03x faster                                               |
| crypto_pyaes            | 75.6 ms                                                                | 73.3 ms: 1.03x faster                                               |
| nbody                   | 90.6 ms                                                                | 88.2 ms: 1.03x faster                                               |
| pycparser               | 1.14 sec                                                               | 1.11 sec: 1.03x faster                                              |
| logging_silent          | 96.9 ns                                                                | 94.8 ns: 1.02x faster                                               |
| meteor_contest          | 106 ms                                                                 | 104 ms: 1.02x faster                                                |
| generators              | 29.3 ms                                                                | 28.7 ms: 1.02x faster                                               |
| pickle_dict             | 32.1 us                                                                | 31.5 us: 1.02x faster                                               |
| pathlib                 | 18.0 ms                                                                | 17.7 ms: 1.02x faster                                               |
| spectral_norm           | 96.4 ms                                                                | 94.7 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult | 4.31 ms                                                                | 4.24 ms: 1.02x faster                                               |
| scimark_lu              | 110 ms                                                                 | 108 ms: 1.02x faster                                                |
| scimark_sor             | 113 ms                                                                 | 111 ms: 1.01x faster                                                |
| fannkuch                | 376 ms                                                                 | 371 ms: 1.01x faster                                                |
| deepcopy_reduce         | 2.94 us                                                                | 2.91 us: 1.01x faster                                               |
| pickle                  | 10.4 us                                                                | 10.3 us: 1.01x faster                                               |
| coroutines              | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                               |
| deltablue               | 3.26 ms                                                                | 3.23 ms: 1.01x faster                                               |
| raytrace                | 281 ms                                                                 | 278 ms: 1.01x faster                                                |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| xml_etree_process       | 55.7 ms                                                                | 55.3 ms: 1.01x faster                                               |
| unpickle_pure_python    | 204 us                                                                 | 202 us: 1.01x faster                                                |
| pyflate                 | 422 ms                                                                 | 420 ms: 1.01x faster                                                |
| richards                | 43.6 ms                                                                | 43.4 ms: 1.01x faster                                               |
| mako                    | 10.0 ms                                                                | 10.0 ms: 1.00x faster                                               |
| hexiom                  | 6.07 ms                                                                | 6.05 ms: 1.00x faster                                               |
| dulwich_log             | 63.8 ms                                                                | 63.6 ms: 1.00x faster                                               |
| python_startup_no_site  | 6.52 ms                                                                | 6.53 ms: 1.00x slower                                               |
| python_startup          | 8.82 ms                                                                | 8.83 ms: 1.00x slower                                               |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                               |
| sqlglot_optimize        | 51.2 ms                                                                | 51.4 ms: 1.00x slower                                               |
| sympy_str               | 281 ms                                                                 | 282 ms: 1.01x slower                                                |
| deepcopy                | 329 us                                                                 | 331 us: 1.01x slower                                                |
| thrift                  | 774 us                                                                 | 780 us: 1.01x slower                                                |
| telco                   | 6.49 ms                                                                | 6.54 ms: 1.01x slower                                               |
| chameleon               | 6.42 ms                                                                | 6.48 ms: 1.01x slower                                               |
| sympy_sum               | 164 ms                                                                 | 166 ms: 1.01x slower                                                |
| json_dumps              | 9.53 ms                                                                | 9.62 ms: 1.01x slower                                               |
| chaos                   | 65.4 ms                                                                | 66.0 ms: 1.01x slower                                               |
| django_template         | 32.5 ms                                                                | 32.8 ms: 1.01x slower                                               |
| sqlglot_parse           | 1.43 ms                                                                | 1.44 ms: 1.01x slower                                               |
| unpack_sequence         | 43.5 ns                                                                | 44.0 ns: 1.01x slower                                               |
| nqueens                 | 81.4 ms                                                                | 82.3 ms: 1.01x slower                                               |
| float                   | 73.6 ms                                                                | 74.4 ms: 1.01x slower                                               |
| docutils                | 2.53 sec                                                               | 2.56 sec: 1.01x slower                                              |
| sqlglot_transpile       | 1.72 ms                                                                | 1.74 ms: 1.01x slower                                               |
| scimark_monte_carlo     | 66.6 ms                                                                | 67.5 ms: 1.01x slower                                               |
| pickle_pure_python      | 284 us                                                                 | 289 us: 1.01x slower                                                |
| sympy_expand            | 454 ms                                                                 | 461 ms: 1.02x slower                                                |
| coverage                | 94.5 ms                                                                | 96.1 ms: 1.02x slower                                               |
| unpickle_list           | 5.06 us                                                                | 5.17 us: 1.02x slower                                               |
| xml_etree_iterparse     | 101 ms                                                                 | 103 ms: 1.02x slower                                                |
| genshi_xml              | 47.1 ms                                                                | 48.6 ms: 1.03x slower                                               |
| mdp                     | 2.52 sec                                                               | 2.68 sec: 1.07x slower                                              |
| regex_effbot            | 3.38 ms                                                                | 3.64 ms: 1.08x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (35): djangocms, html5lib, sqlalchemy_imperative, async_tree_memoization, async_tree_io, json_loads, async_tree_cpu_io_mixed, async_tree_none, deepcopy_memo, genshi_text, gunicorn, 2to3, bench_thread_pool, xml_etree_generate, regex_v8, mypy2, xml_etree_parse, pidigits, asyncio_tcp, bench_mp_pool, pprint_safe_repr, create_gc_cycles, comprehensions, regex_dna, sympy_integrate, regex_compile, pprint_pformat, json, go, async_generators, dask, tornado_http, sqlite_synth, sqlalchemy_declarative, unpickle
