# Results vs. 3.13.0

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                  |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.02x slower                                                |
| html5lib       | 64.2 ms                                                | 63.3 ms: 1.01x faster                                                 |
| tornado_http   | 92.4 ms                                                | 90.8 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none            | 351 ms                                                 | 314 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 305 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                  |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| async_tree_io              | 842 ms                                                 | 864 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.1 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.07x faster                                                 |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.9 ms: 1.03x faster                                                 |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.02x faster                                                  |
| unpickle_pure_python | 216 us                                                 | 211 us: 1.02x faster                                                  |
| xml_etree_generate   | 86.7 ms                                                | 85.0 ms: 1.02x faster                                                 |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.02x faster                                                |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                 |
| django_template | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                 |
| deepcopy                   | 358 us                                                 | 257 us: 1.39x faster                                                  |
| deepcopy_memo              | 39.1 us                                                | 29.7 us: 1.32x faster                                                 |
| go                         | 144 ms                                                 | 118 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                                  |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none            | 351 ms                                                 | 314 ms: 1.12x faster                                                  |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                 |
| gc_traversal               | 4.37 ms                                                | 3.98 ms: 1.10x faster                                                 |
| json                       | 5.36 ms                                                | 4.96 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.67 ms: 1.08x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.07x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| thrift                     | 809 us                                                 | 764 us: 1.06x faster                                                  |
| generators                 | 29.0 ms                                                | 27.5 ms: 1.05x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 305 ms: 1.05x faster                                                  |
| 2to3                       | 267 ms                                                 | 254 ms: 1.05x faster                                                  |
| crypto_pyaes               | 75.3 ms                                                | 71.7 ms: 1.05x faster                                                 |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                                 |
| richards                   | 48.7 ms                                                | 46.8 ms: 1.04x faster                                                 |
| bench_thread_pool          | 822 us                                                 | 792 us: 1.04x faster                                                  |
| pyflate                    | 471 ms                                                 | 454 ms: 1.04x faster                                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| logging_silent             | 102 ns                                                 | 98.2 ns: 1.04x faster                                                 |
| genshi_text                | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                 |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| raytrace                   | 267 ms                                                 | 259 ms: 1.03x faster                                                  |
| django_template            | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 58.9 ms: 1.03x faster                                                 |
| logging_format             | 6.40 us                                                | 6.22 us: 1.03x faster                                                 |
| mdp                        | 2.72 sec                                               | 2.65 sec: 1.03x faster                                                |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.02x faster                                                  |
| unpickle_pure_python       | 216 us                                                 | 211 us: 1.02x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 85.0 ms: 1.02x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                  |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                  |
| tornado_http               | 92.4 ms                                                | 90.8 ms: 1.02x faster                                                 |
| fannkuch                   | 404 ms                                                 | 397 ms: 1.02x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.02x faster                                                |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                 |
| html5lib                   | 64.2 ms                                                | 63.3 ms: 1.01x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.01x faster                                                  |
| float                      | 79.2 ms                                                | 78.1 ms: 1.01x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                 |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                 |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                                  |
| scimark_fft                | 364 ms                                                 | 362 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 67.1 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 728 ms                                                 | 725 ms: 1.00x faster                                                  |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                 |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 64.6 ms: 1.00x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                                 |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.80 sec: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                  |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.02x slower                                                |
| nqueens                    | 78.4 ms                                                | 80.5 ms: 1.03x slower                                                 |
| async_tree_io              | 842 ms                                                 | 864 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (11): nbody, telco, sqlglot_normalize, sqlglot_transpile, deltablue, regex_dna, scimark_lu, genshi_xml, bench_mp_pool, hexiom, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-4ed7d1d/bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x