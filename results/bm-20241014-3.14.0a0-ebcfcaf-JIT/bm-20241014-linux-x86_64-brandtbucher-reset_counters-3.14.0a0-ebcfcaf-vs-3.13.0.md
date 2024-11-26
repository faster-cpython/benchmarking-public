# Results vs. 3.13.0

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: ebcfcaf
- commit date: 2024-10-14
- overall geometric mean: 1.026x faster
- HPT reliability: 94.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.87 sec: 1.11x slower                                                |
| html5lib       | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                 |
| tornado_http   | 92.4 ms                                                | 93.7 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|--------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| coroutines         | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| async_generators   | 436 ms                                                 | 454 ms: 1.04x slower                                                  |
| Geometric mean     | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 72.4 ms: 1.09x faster                                                 |
| nbody          | 87.0 ms                                                | 83.5 ms: 1.04x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                 |
| regex_dna      | 218 ms                                                 | 209 ms: 1.05x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                 |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 78.4 ms: 1.11x faster                                                 |
| xml_etree_process    | 60.6 ms                                                | 54.9 ms: 1.10x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                 |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                  |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                 |
| django_template | 35.2 ms                                                | 36.0 ms: 1.03x slower                                                 |
| genshi_text     | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 58.0 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo           | 39.1 us                                                | 27.4 us: 1.43x faster                                                 |
| deepcopy                | 358 us                                                 | 264 us: 1.36x faster                                                  |
| create_gc_cycles        | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                 |
| richards_super          | 54.9 ms                                                | 45.2 ms: 1.21x faster                                                 |
| deepcopy_reduce         | 3.20 us                                                | 2.66 us: 1.21x faster                                                 |
| richards                | 48.7 ms                                                | 40.7 ms: 1.19x faster                                                 |
| python_startup          | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| scimark_fft             | 364 ms                                                 | 312 ms: 1.17x faster                                                  |
| spectral_norm           | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| crypto_pyaes            | 75.3 ms                                                | 66.7 ms: 1.13x faster                                                 |
| telco                   | 8.54 ms                                                | 7.62 ms: 1.12x faster                                                 |
| tomli_loads             | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                |
| xml_etree_generate      | 86.7 ms                                                | 78.4 ms: 1.11x faster                                                 |
| mako                    | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                 |
| xml_etree_process       | 60.6 ms                                                | 54.9 ms: 1.10x faster                                                 |
| pathlib                 | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                 |
| float                   | 79.2 ms                                                | 72.4 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult | 5.04 ms                                                | 4.62 ms: 1.09x faster                                                 |
| gc_traversal            | 4.37 ms                                                | 4.01 ms: 1.09x faster                                                 |
| json                    | 5.36 ms                                                | 4.93 ms: 1.09x faster                                                 |
| go                      | 144 ms                                                 | 132 ms: 1.09x faster                                                  |
| regex_v8                | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                 |
| bpe_tokeniser           | 4.75 sec                                               | 4.39 sec: 1.08x faster                                                |
| xml_etree_parse         | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| mdp                     | 2.72 sec                                               | 2.55 sec: 1.07x faster                                                |
| fannkuch                | 404 ms                                                 | 381 ms: 1.06x faster                                                  |
| scimark_monte_carlo     | 67.4 ms                                                | 63.5 ms: 1.06x faster                                                 |
| logging_format          | 6.40 us                                                | 6.04 us: 1.06x faster                                                 |
| scimark_sor             | 124 ms                                                 | 117 ms: 1.05x faster                                                  |
| pyflate                 | 471 ms                                                 | 447 ms: 1.05x faster                                                  |
| regex_dna               | 218 ms                                                 | 209 ms: 1.05x faster                                                  |
| pycparser               | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                |
| logging_simple          | 5.72 us                                                | 5.48 us: 1.04x faster                                                 |
| nbody                   | 87.0 ms                                                | 83.5 ms: 1.04x faster                                                 |
| regex_effbot            | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                 |
| xml_etree_iterparse     | 101 ms                                                 | 98.0 ms: 1.03x faster                                                 |
| thrift                  | 809 us                                                 | 785 us: 1.03x faster                                                  |
| json_loads              | 27.2 us                                                | 26.6 us: 1.02x faster                                                 |
| html5lib                | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                 |
| scimark_lu              | 113 ms                                                 | 110 ms: 1.02x faster                                                  |
| logging_silent          | 102 ns                                                 | 99.8 ns: 1.02x faster                                                 |
| meteor_contest          | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| coverage                | 84.0 ms                                                | 83.5 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 216 us                                                 | 215 us: 1.00x faster                                                  |
| pidigits                | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| asyncio_websockets      | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| tornado_http            | 92.4 ms                                                | 93.7 ms: 1.01x slower                                                 |
| python_startup_no_site  | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| chaos                   | 58.1 ms                                                | 59.1 ms: 1.02x slower                                                 |
| comprehensions          | 16.5 us                                                | 16.9 us: 1.02x slower                                                 |
| coroutines              | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| django_template         | 35.2 ms                                                | 36.0 ms: 1.03x slower                                                 |
| sqlglot_parse           | 1.27 ms                                                | 1.32 ms: 1.03x slower                                                 |
| 2to3                    | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| async_generators        | 436 ms                                                 | 454 ms: 1.04x slower                                                  |
| dulwich_log             | 64.3 ms                                                | 67.5 ms: 1.05x slower                                                 |
| regex_compile           | 132 ms                                                 | 139 ms: 1.05x slower                                                  |
| sqlglot_transpile       | 1.58 ms                                                | 1.67 ms: 1.05x slower                                                 |
| raytrace                | 267 ms                                                 | 282 ms: 1.06x slower                                                  |
| sqlglot_normalize       | 108 ms                                                 | 114 ms: 1.06x slower                                                  |
| bench_thread_pool       | 822 us                                                 | 871 us: 1.06x slower                                                  |
| json_dumps              | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                 |
| genshi_text             | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                 |
| sympy_expand            | 463 ms                                                 | 498 ms: 1.08x slower                                                  |
| sympy_str               | 275 ms                                                 | 300 ms: 1.09x slower                                                  |
| nqueens                 | 78.4 ms                                                | 86.5 ms: 1.10x slower                                                 |
| sqlglot_optimize        | 53.7 ms                                                | 59.3 ms: 1.10x slower                                                 |
| docutils                | 2.59 sec                                               | 2.87 sec: 1.11x slower                                                |
| hexiom                  | 6.16 ms                                                | 7.00 ms: 1.14x slower                                                 |
| genshi_xml              | 50.9 ms                                                | 58.0 ms: 1.14x slower                                                 |
| sympy_sum               | 150 ms                                                 | 175 ms: 1.16x slower                                                  |
| sympy_integrate         | 19.9 ms                                                | 23.2 ms: 1.17x slower                                                 |
| pylint                  | 313 ms                                                 | 373 ms: 1.19x slower                                                  |
| generators              | 29.0 ms                                                | 35.3 ms: 1.22x slower                                                 |
| bench_mp_pool           | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (5): pprint_pformat, typing_runtime_protocols, pickle_pure_python, deltablue, pprint_safe_repr
Ignored benchmarks (17) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241014-3.14.0a0-ebcfcaf-JIT/bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 94.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x