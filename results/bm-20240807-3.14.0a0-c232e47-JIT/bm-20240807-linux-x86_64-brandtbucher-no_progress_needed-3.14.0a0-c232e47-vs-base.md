# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: c232e47
- commit date: 2024-08-07
- overall geometric mean: 1.05x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 282 ms: 1.03x slower                                                      |
| docutils       | 2.92 sec                                                              | 6.89 sec: 2.36x slower                                                    |
| html5lib       | 63.8 ms                                                               | 67.4 ms: 1.06x slower                                                     |
| tornado_http   | 92.6 ms                                                               | 93.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.27x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines             | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                     |
| asyncio_tcp            | 498 ms                                                                | 502 ms: 1.01x slower                                                      |
| async_tree_none        | 327 ms                                                                | 331 ms: 1.01x slower                                                      |
| async_tree_none_tg     | 300 ms                                                                | 305 ms: 1.02x slower                                                      |
| async_tree_io_tg       | 864 ms                                                                | 880 ms: 1.02x slower                                                      |
| async_tree_memoization | 422 ms                                                                | 432 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| float          | 70.5 ms                                                               | 71.0 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                | 224 ms: 1.00x slower                                                      |
| regex_v8       | 24.4 ms                                                               | 24.7 ms: 1.01x slower                                                     |
| regex_compile  | 135 ms                                                                | 136 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 211 us: 1.02x faster                                                      |
| tomli_loads          | 1.91 sec                                                              | 1.89 sec: 1.01x faster                                                    |
| xml_etree_iterparse  | 99.2 ms                                                               | 99.6 ms: 1.00x slower                                                     |
| xml_etree_process    | 57.2 ms                                                               | 57.8 ms: 1.01x slower                                                     |
| json_loads           | 27.7 us                                                               | 28.0 us: 1.01x slower                                                     |
| xml_etree_generate   | 81.6 ms                                                               | 84.1 ms: 1.03x slower                                                     |
| pickle_pure_python   | 300 us                                                                | 316 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.20 ms: 1.01x slower                                                     |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                               | 35.3 ms: 1.02x faster                                                     |
| mako            | 9.85 ms                                                               | 9.71 ms: 1.01x faster                                                     |
| genshi_text     | 24.5 ms                                                               | 25.5 ms: 1.04x slower                                                     |
| genshi_xml      | 53.4 ms                                                               | 57.1 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 3.58 ms                                                               | 3.06 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.15 ms: 1.10x faster                                                     |
| deepcopy_memo           | 29.1 us                                                               | 27.5 us: 1.06x faster                                                     |
| deepcopy                | 273 us                                                                | 260 us: 1.05x faster                                                      |
| richards_super          | 47.5 ms                                                               | 45.4 ms: 1.05x faster                                                     |
| logging_silent          | 104 ns                                                                | 99.8 ns: 1.05x faster                                                     |
| richards                | 41.2 ms                                                               | 39.7 ms: 1.04x faster                                                     |
| deepcopy_reduce         | 2.78 us                                                               | 2.68 us: 1.04x faster                                                     |
| gc_traversal            | 3.85 ms                                                               | 3.75 ms: 1.03x faster                                                     |
| logging_format          | 6.17 us                                                               | 6.01 us: 1.03x faster                                                     |
| sympy_expand            | 508 ms                                                                | 496 ms: 1.03x faster                                                      |
| unpickle_pure_python    | 215 us                                                                | 211 us: 1.02x faster                                                      |
| django_template         | 36.0 ms                                                               | 35.3 ms: 1.02x faster                                                     |
| logging_simple          | 5.57 us                                                               | 5.47 us: 1.02x faster                                                     |
| telco                   | 7.97 ms                                                               | 7.83 ms: 1.02x faster                                                     |
| mako                    | 9.85 ms                                                               | 9.71 ms: 1.01x faster                                                     |
| scimark_lu              | 109 ms                                                                | 107 ms: 1.01x faster                                                      |
| go                      | 146 ms                                                                | 144 ms: 1.01x faster                                                      |
| tomli_loads             | 1.91 sec                                                              | 1.89 sec: 1.01x faster                                                    |
| coroutines              | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                     |
| scimark_sor             | 117 ms                                                                | 116 ms: 1.01x faster                                                      |
| crypto_pyaes            | 66.8 ms                                                               | 66.1 ms: 1.01x faster                                                     |
| spectral_norm           | 100 ms                                                                | 99.5 ms: 1.01x faster                                                     |
| pathlib                 | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                     |
| scimark_fft             | 307 ms                                                                | 304 ms: 1.01x faster                                                      |
| bench_thread_pool       | 822 us                                                                | 817 us: 1.01x faster                                                      |
| sympy_str               | 298 ms                                                                | 296 ms: 1.01x faster                                                      |
| pidigits                | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| xml_etree_iterparse     | 99.2 ms                                                               | 99.6 ms: 1.00x slower                                                     |
| sympy_sum               | 170 ms                                                                | 171 ms: 1.00x slower                                                      |
| regex_dna               | 223 ms                                                                | 224 ms: 1.00x slower                                                      |
| tornado_http            | 92.6 ms                                                               | 93.1 ms: 1.01x slower                                                     |
| python_startup_no_site  | 7.17 ms                                                               | 7.20 ms: 1.01x slower                                                     |
| python_startup          | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| float                   | 70.5 ms                                                               | 71.0 ms: 1.01x slower                                                     |
| meteor_contest          | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| asyncio_tcp             | 498 ms                                                                | 502 ms: 1.01x slower                                                      |
| sympy_integrate         | 22.6 ms                                                               | 22.8 ms: 1.01x slower                                                     |
| comprehensions          | 16.2 us                                                               | 16.4 us: 1.01x slower                                                     |
| regex_v8                | 24.4 ms                                                               | 24.7 ms: 1.01x slower                                                     |
| xml_etree_process       | 57.2 ms                                                               | 57.8 ms: 1.01x slower                                                     |
| regex_compile           | 135 ms                                                                | 136 ms: 1.01x slower                                                      |
| json_loads              | 27.7 us                                                               | 28.0 us: 1.01x slower                                                     |
| pprint_safe_repr        | 722 ms                                                                | 733 ms: 1.01x slower                                                      |
| async_tree_none         | 327 ms                                                                | 331 ms: 1.01x slower                                                      |
| async_tree_none_tg      | 300 ms                                                                | 305 ms: 1.02x slower                                                      |
| async_tree_io_tg        | 864 ms                                                                | 880 ms: 1.02x slower                                                      |
| async_tree_memoization  | 422 ms                                                                | 432 ms: 1.02x slower                                                      |
| 2to3                    | 275 ms                                                                | 282 ms: 1.03x slower                                                      |
| nqueens                 | 84.0 ms                                                               | 86.3 ms: 1.03x slower                                                     |
| xml_etree_generate      | 81.6 ms                                                               | 84.1 ms: 1.03x slower                                                     |
| pyflate                 | 432 ms                                                                | 445 ms: 1.03x slower                                                      |
| pprint_pformat          | 1.49 sec                                                              | 1.54 sec: 1.03x slower                                                    |
| scimark_monte_carlo     | 60.7 ms                                                               | 62.8 ms: 1.03x slower                                                     |
| genshi_text             | 24.5 ms                                                               | 25.5 ms: 1.04x slower                                                     |
| pickle_pure_python      | 300 us                                                                | 316 us: 1.05x slower                                                      |
| mdp                     | 2.56 sec                                                              | 2.70 sec: 1.05x slower                                                    |
| html5lib                | 63.8 ms                                                               | 67.4 ms: 1.06x slower                                                     |
| sqlglot_transpile       | 1.62 ms                                                               | 1.73 ms: 1.07x slower                                                     |
| genshi_xml              | 53.4 ms                                                               | 57.1 ms: 1.07x slower                                                     |
| sqlglot_optimize        | 55.9 ms                                                               | 60.6 ms: 1.08x slower                                                     |
| sqlglot_parse           | 1.29 ms                                                               | 1.40 ms: 1.09x slower                                                     |
| pylint                  | 356 ms                                                                | 443 ms: 1.24x slower                                                      |
| pycparser               | 1.19 sec                                                              | 1.64 sec: 1.38x slower                                                    |
| docutils                | 2.92 sec                                                              | 6.89 sec: 2.36x slower                                                    |
| raytrace                | 269 ms                                                                | 5.00 sec: 18.59x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.05x slower                                                              |

Benchmark hidden because not significant (23): coverage, json_dumps, generators, regex_effbot, json, typing_runtime_protocols, hexiom, sqlglot_normalize, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, chaos, bench_mp_pool, create_gc_cycles, bpe_tokeniser, async_tree_cpu_io_mixed, thrift, asyncio_websockets, async_generators, nbody, async_tree_io, fannkuch, async_tree_memoization_tg, xml_etree_parse

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x