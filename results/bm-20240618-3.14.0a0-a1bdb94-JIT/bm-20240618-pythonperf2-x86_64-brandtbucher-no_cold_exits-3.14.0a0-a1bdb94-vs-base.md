# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.01x faster
- HPT reliability: 97.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                      | 306 ms: 1.01x slower                                                       |
| html5lib       | 74.9 ms                                                                     | 74.6 ms: 1.01x faster                                                      |
| tornado_http   | 122 ms                                                                      | 123 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.2 ms                                                                     | 74.8 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                      | 238 ms: 1.07x faster                                                       |
| regex_effbot   | 3.65 ms                                                                     | 3.45 ms: 1.06x faster                                                      |
| regex_v8       | 26.2 ms                                                                     | 25.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 4.60 us                                                                     | 4.35 us: 1.06x faster                                                      |
| unpickle             | 15.7 us                                                                     | 15.1 us: 1.04x faster                                                      |
| tomli_loads          | 2.16 sec                                                                    | 2.11 sec: 1.03x faster                                                     |
| xml_etree_generate   | 82.1 ms                                                                     | 80.8 ms: 1.02x faster                                                      |
| xml_etree_process    | 58.5 ms                                                                     | 58.0 ms: 1.01x faster                                                      |
| pickle               | 10.7 us                                                                     | 10.6 us: 1.01x faster                                                      |
| json_dumps           | 10.6 ms                                                                     | 10.7 ms: 1.01x slower                                                      |
| json_loads           | 25.0 us                                                                     | 25.2 us: 1.01x slower                                                      |
| unpickle_pure_python | 217 us                                                                      | 220 us: 1.01x slower                                                       |
| xml_etree_parse      | 143 ms                                                                      | 145 ms: 1.01x slower                                                       |
| pickle_dict          | 30.9 us                                                                     | 31.4 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): unpickle_list, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.47 ms                                                                     | 8.94 ms: 1.06x faster                                                      |
| python_startup         | 13.8 ms                                                                     | 13.4 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 65.2 ms                                                                     | 63.6 ms: 1.03x faster                                                      |
| mako           | 9.20 ms                                                                     | 9.24 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna               | 254 ms                                                                      | 238 ms: 1.07x faster                                                       |
| regex_effbot            | 3.65 ms                                                                     | 3.45 ms: 1.06x faster                                                      |
| python_startup_no_site  | 9.47 ms                                                                     | 8.94 ms: 1.06x faster                                                      |
| pyflate                 | 467 ms                                                                      | 442 ms: 1.06x faster                                                       |
| pickle_list             | 4.60 us                                                                     | 4.35 us: 1.06x faster                                                      |
| unpickle                | 15.7 us                                                                     | 15.1 us: 1.04x faster                                                      |
| logging_silent          | 109 ns                                                                      | 105 ns: 1.04x faster                                                       |
| python_startup          | 13.8 ms                                                                     | 13.4 ms: 1.03x faster                                                      |
| async_generators        | 397 ms                                                                      | 385 ms: 1.03x faster                                                       |
| tomli_loads             | 2.16 sec                                                                    | 2.11 sec: 1.03x faster                                                     |
| genshi_xml              | 65.2 ms                                                                     | 63.6 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult | 4.02 ms                                                                     | 3.92 ms: 1.03x faster                                                      |
| crypto_pyaes            | 72.1 ms                                                                     | 70.4 ms: 1.02x faster                                                      |
| bpe_tokeniser           | 5.23 sec                                                                    | 5.11 sec: 1.02x faster                                                     |
| raytrace                | 297 ms                                                                      | 291 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 797 ms                                                                      | 781 ms: 1.02x faster                                                       |
| float                   | 76.2 ms                                                                     | 74.8 ms: 1.02x faster                                                      |
| xml_etree_generate      | 82.1 ms                                                                     | 80.8 ms: 1.02x faster                                                      |
| sqlglot_optimize        | 63.5 ms                                                                     | 62.5 ms: 1.02x faster                                                      |
| nqueens                 | 94.6 ms                                                                     | 93.3 ms: 1.01x faster                                                      |
| pprint_pformat          | 1.64 sec                                                                    | 1.62 sec: 1.01x faster                                                     |
| regex_v8                | 26.2 ms                                                                     | 25.9 ms: 1.01x faster                                                      |
| chaos                   | 67.1 ms                                                                     | 66.3 ms: 1.01x faster                                                      |
| generators              | 35.2 ms                                                                     | 34.9 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 129 ms                                                                      | 128 ms: 1.01x faster                                                       |
| thrift                  | 913 us                                                                      | 905 us: 1.01x faster                                                       |
| xml_etree_process       | 58.5 ms                                                                     | 58.0 ms: 1.01x faster                                                      |
| hexiom                  | 6.71 ms                                                                     | 6.66 ms: 1.01x faster                                                      |
| deepcopy                | 306 us                                                                      | 304 us: 1.01x faster                                                       |
| mdp                     | 2.58 sec                                                                    | 2.57 sec: 1.01x faster                                                     |
| pickle                  | 10.7 us                                                                     | 10.6 us: 1.01x faster                                                      |
| html5lib                | 74.9 ms                                                                     | 74.6 ms: 1.01x faster                                                      |
| logging_format          | 7.05 us                                                                     | 7.02 us: 1.00x faster                                                      |
| fannkuch                | 339 ms                                                                      | 337 ms: 1.00x faster                                                       |
| comprehensions          | 18.2 us                                                                     | 18.2 us: 1.00x faster                                                      |
| asyncio_tcp_ssl         | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                     |
| create_gc_cycles        | 1.91 ms                                                                     | 1.92 ms: 1.00x slower                                                      |
| scimark_fft             | 292 ms                                                                      | 293 ms: 1.00x slower                                                       |
| sympy_expand            | 528 ms                                                                      | 529 ms: 1.00x slower                                                       |
| sqlglot_transpile       | 1.83 ms                                                                     | 1.84 ms: 1.00x slower                                                      |
| pathlib                 | 16.3 ms                                                                     | 16.3 ms: 1.00x slower                                                      |
| mako                    | 9.20 ms                                                                     | 9.24 ms: 1.00x slower                                                      |
| asyncio_tcp             | 378 ms                                                                      | 380 ms: 1.01x slower                                                       |
| meteor_contest          | 130 ms                                                                      | 130 ms: 1.01x slower                                                       |
| asyncio_websockets      | 389 ms                                                                      | 392 ms: 1.01x slower                                                       |
| 2to3                    | 304 ms                                                                      | 306 ms: 1.01x slower                                                       |
| json_dumps              | 10.6 ms                                                                     | 10.7 ms: 1.01x slower                                                      |
| json_loads              | 25.0 us                                                                     | 25.2 us: 1.01x slower                                                      |
| sqlglot_parse           | 1.42 ms                                                                     | 1.44 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 65.0 ms                                                                     | 65.8 ms: 1.01x slower                                                      |
| tornado_http            | 122 ms                                                                      | 123 ms: 1.01x slower                                                       |
| deltablue               | 3.64 ms                                                                     | 3.69 ms: 1.01x slower                                                      |
| coverage                | 82.4 ms                                                                     | 83.4 ms: 1.01x slower                                                      |
| unpickle_pure_python    | 217 us                                                                      | 220 us: 1.01x slower                                                       |
| xml_etree_parse         | 143 ms                                                                      | 145 ms: 1.01x slower                                                       |
| pickle_dict             | 30.9 us                                                                     | 31.4 us: 1.01x slower                                                      |
| sympy_sum               | 165 ms                                                                      | 168 ms: 1.02x slower                                                       |
| dulwich_log             | 66.0 ms                                                                     | 67.1 ms: 1.02x slower                                                      |
| deepcopy_memo           | 29.1 us                                                                     | 29.6 us: 1.02x slower                                                      |
| gc_traversal            | 4.34 ms                                                                     | 4.42 ms: 1.02x slower                                                      |
| go                      | 162 ms                                                                      | 166 ms: 1.03x slower                                                       |
| coroutines              | 21.7 ms                                                                     | 22.8 ms: 1.05x slower                                                      |
| scimark_sor             | 129 ms                                                                      | 136 ms: 1.06x slower                                                       |
| Geometric mean          | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (34): bench_thread_pool, richards_super, async_tree_io, pycparser, async_tree_memoization, unpickle_list, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, logging_simple, async_tree_io_tg, deepcopy_reduce, async_tree_none_tg, async_tree_none, sqlite_synth, pickle_pure_python, genshi_text, typing_runtime_protocols, sympy_integrate, xml_etree_iterparse, telco, dask, pidigits, docutils, django_template, richards, scimark_lu, sympy_str, pylint, regex_compile, spectral_norm, json, nbody, bench_mp_pool

# HPT report

- Reliability score: 97.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x