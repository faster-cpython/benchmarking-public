# Results vs. base

- fork: brandtbucher
- ref: off_by_one
- machine: linux-x86_64
- commit hash: e099186
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 2.96 sec                                                              | 2.93 sec: 1.01x faster                                            |
| html5lib       | 64.5 ms                                                               | 62.2 ms: 1.04x faster                                             |
| tornado_http   | 94.6 ms                                                               | 93.5 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp        | 498 ms                                                                | 487 ms: 1.02x faster                                              |
| asyncio_tcp_ssl    | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                            |
| asyncio_websockets | 555 ms                                                                | 558 ms: 1.00x slower                                              |
| coroutines         | 22.9 ms                                                               | 23.0 ms: 1.01x slower                                             |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (9): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_generators, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 80.2 ms                                                               | 79.0 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.50 ms: 1.08x faster                                             |
| regex_compile  | 141 ms                                                                | 139 ms: 1.02x faster                                              |
| regex_dna      | 216 ms                                                                | 217 ms: 1.00x slower                                              |
| regex_v8       | 24.7 ms                                                               | 25.1 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_process    | 55.6 ms                                                               | 54.9 ms: 1.01x faster                                             |
| json_dumps           | 10.1 ms                                                               | 9.99 ms: 1.01x faster                                             |
| unpickle_pure_python | 216 us                                                                | 214 us: 1.01x faster                                              |
| xml_etree_iterparse  | 97.9 ms                                                               | 98.7 ms: 1.01x slower                                             |
| xml_etree_generate   | 78.7 ms                                                               | 79.4 ms: 1.01x slower                                             |
| pickle_list          | 5.17 us                                                               | 5.22 us: 1.01x slower                                             |
| xml_etree_parse      | 145 ms                                                                | 146 ms: 1.01x slower                                              |
| unpickle_list        | 5.17 us                                                               | 5.22 us: 1.01x slower                                             |
| pickle_pure_python   | 305 us                                                                | 310 us: 1.02x slower                                              |
| json_loads           | 26.7 us                                                               | 27.1 us: 1.02x slower                                             |
| pickle               | 11.6 us                                                               | 11.9 us: 1.02x slower                                             |
| pickle_dict          | 34.5 us                                                               | 35.8 us: 1.04x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                             |
| python_startup_no_site | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                               | 58.6 ms: 1.02x faster                                             |
| mako            | 9.88 ms                                                               | 9.77 ms: 1.01x faster                                             |
| django_template | 35.3 ms                                                               | 36.5 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot            | 3.80 ms                                                               | 3.50 ms: 1.08x faster                                             |
| pprint_pformat          | 1.60 sec                                                              | 1.48 sec: 1.08x faster                                            |
| unpack_sequence         | 112 ns                                                                | 105 ns: 1.07x faster                                              |
| pprint_safe_repr        | 748 ms                                                                | 714 ms: 1.05x faster                                              |
| mdp                     | 2.66 sec                                                              | 2.54 sec: 1.05x faster                                            |
| pyflate                 | 448 ms                                                                | 430 ms: 1.04x faster                                              |
| raytrace                | 281 ms                                                                | 271 ms: 1.04x faster                                              |
| html5lib                | 64.5 ms                                                               | 62.2 ms: 1.04x faster                                             |
| richards_super          | 45.6 ms                                                               | 44.2 ms: 1.03x faster                                             |
| richards                | 39.9 ms                                                               | 38.9 ms: 1.03x faster                                             |
| genshi_xml              | 60.0 ms                                                               | 58.6 ms: 1.02x faster                                             |
| deepcopy_memo           | 27.2 us                                                               | 26.6 us: 1.02x faster                                             |
| telco                   | 8.05 ms                                                               | 7.87 ms: 1.02x faster                                             |
| logging_simple          | 5.75 us                                                               | 5.62 us: 1.02x faster                                             |
| asyncio_tcp             | 498 ms                                                                | 487 ms: 1.02x faster                                              |
| logging_format          | 6.24 us                                                               | 6.13 us: 1.02x faster                                             |
| nbody                   | 80.2 ms                                                               | 79.0 ms: 1.02x faster                                             |
| regex_compile           | 141 ms                                                                | 139 ms: 1.02x faster                                              |
| xml_etree_process       | 55.6 ms                                                               | 54.9 ms: 1.01x faster                                             |
| sqlglot_parse           | 1.35 ms                                                               | 1.33 ms: 1.01x faster                                             |
| scimark_sor             | 117 ms                                                                | 116 ms: 1.01x faster                                              |
| pathlib                 | 15.9 ms                                                               | 15.7 ms: 1.01x faster                                             |
| json_dumps              | 10.1 ms                                                               | 9.99 ms: 1.01x faster                                             |
| tornado_http            | 94.6 ms                                                               | 93.5 ms: 1.01x faster                                             |
| mako                    | 9.88 ms                                                               | 9.77 ms: 1.01x faster                                             |
| docutils                | 2.96 sec                                                              | 2.93 sec: 1.01x faster                                            |
| meteor_contest          | 107 ms                                                                | 106 ms: 1.01x faster                                              |
| scimark_fft             | 308 ms                                                                | 304 ms: 1.01x faster                                              |
| unpickle_pure_python    | 216 us                                                                | 214 us: 1.01x faster                                              |
| scimark_monte_carlo     | 63.0 ms                                                               | 62.3 ms: 1.01x faster                                             |
| deepcopy_reduce         | 2.68 us                                                               | 2.65 us: 1.01x faster                                             |
| sqlglot_normalize       | 113 ms                                                                | 112 ms: 1.01x faster                                              |
| go                      | 131 ms                                                                | 130 ms: 1.01x faster                                              |
| deltablue               | 3.21 ms                                                               | 3.18 ms: 1.01x faster                                             |
| sqlglot_transpile       | 1.69 ms                                                               | 1.68 ms: 1.01x faster                                             |
| sympy_integrate         | 22.8 ms                                                               | 22.7 ms: 1.01x faster                                             |
| chaos                   | 58.0 ms                                                               | 57.7 ms: 1.01x faster                                             |
| logging_silent          | 104 ns                                                                | 104 ns: 1.01x faster                                              |
| comprehensions          | 16.6 us                                                               | 16.6 us: 1.00x faster                                             |
| dulwich_log             | 67.8 ms                                                               | 67.6 ms: 1.00x faster                                             |
| bench_thread_pool       | 839 us                                                                | 836 us: 1.00x faster                                              |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                             |
| sqlglot_optimize        | 58.2 ms                                                               | 58.0 ms: 1.00x faster                                             |
| python_startup_no_site  | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                             |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                            |
| gc_traversal            | 3.94 ms                                                               | 3.94 ms: 1.00x slower                                             |
| hexiom                  | 6.86 ms                                                               | 6.88 ms: 1.00x slower                                             |
| regex_dna               | 216 ms                                                                | 217 ms: 1.00x slower                                              |
| scimark_lu              | 110 ms                                                                | 111 ms: 1.00x slower                                              |
| asyncio_websockets      | 555 ms                                                                | 558 ms: 1.00x slower                                              |
| coroutines              | 22.9 ms                                                               | 23.0 ms: 1.01x slower                                             |
| coverage                | 85.2 ms                                                               | 85.7 ms: 1.01x slower                                             |
| create_gc_cycles        | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                             |
| deepcopy                | 258 us                                                                | 260 us: 1.01x slower                                              |
| xml_etree_iterparse     | 97.9 ms                                                               | 98.7 ms: 1.01x slower                                             |
| xml_etree_generate      | 78.7 ms                                                               | 79.4 ms: 1.01x slower                                             |
| thrift                  | 790 us                                                                | 797 us: 1.01x slower                                              |
| pickle_list             | 5.17 us                                                               | 5.22 us: 1.01x slower                                             |
| xml_etree_parse         | 145 ms                                                                | 146 ms: 1.01x slower                                              |
| unpickle_list           | 5.17 us                                                               | 5.22 us: 1.01x slower                                             |
| regex_v8                | 24.7 ms                                                               | 25.1 ms: 1.01x slower                                             |
| scimark_sparse_mat_mult | 4.21 ms                                                               | 4.27 ms: 1.01x slower                                             |
| pickle_pure_python      | 305 us                                                                | 310 us: 1.02x slower                                              |
| json_loads              | 26.7 us                                                               | 27.1 us: 1.02x slower                                             |
| generators              | 32.8 ms                                                               | 33.5 ms: 1.02x slower                                             |
| pickle                  | 11.6 us                                                               | 11.9 us: 1.02x slower                                             |
| django_template         | 35.3 ms                                                               | 36.5 ms: 1.03x slower                                             |
| pickle_dict             | 34.5 us                                                               | 35.8 us: 1.04x slower                                             |
| json                    | 4.94 ms                                                               | 5.14 ms: 1.04x slower                                             |
| pycparser               | 1.15 sec                                                              | 1.20 sec: 1.04x slower                                            |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (27): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, typing_runtime_protocols, fannkuch, async_tree_cpu_io_mixed_tg, nqueens, float, sympy_sum, sympy_expand, pylint, spectral_norm, tomli_loads, async_generators, sympy_str, 2to3, pidigits, async_tree_none_tg, bench_mp_pool, async_tree_memoization_tg, crypto_pyaes, genshi_text, bpe_tokeniser, sqlite_synth, async_tree_io, async_tree_io_tg, unpickle

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x